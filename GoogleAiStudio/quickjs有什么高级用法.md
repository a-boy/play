QuickJS 以其小巧、快速和支持最新 ECMAScript 标准而闻名。除了基本的 JavaScript 脚本执行外，它还有许多高级用法，主要体现在其 C API 的灵活性和 `qjsc` 编译器的能力上。

以下是一些 QuickJS 的高级用法：

1.  **嵌入到 C/C++ 应用程序中 (Embedding):**
    *   **作为脚本引擎:** 这是最常见的用法。你可以将 QuickJS 嵌入到你的 C/C++ 程序中，使其能够执行 JavaScript 脚本。这可以用于插件系统、游戏逻辑、配置脚本等。
    *   **C 与 JS 互操作:**
        *   **从 C 调用 JS 函数:** `JS_Call`, `JS_Invoke` 等函数允许 C 代码调用 JS 函数并获取其返回值。
        *   **从 JS 调用 C 函数:** `JS_NewCFunction` 允许你将 C 函数暴露给 JavaScript，JS 代码可以像调用普通 JS 函数一样调用它们。这对于实现原生功能（如文件 I/O、网络、图形等）非常有用。
        *   **数据传递:** 理解 `JSValue` 类型以及如何在 C 和 JS 之间转换数字、字符串、对象、数组等至关重要。`JS_NewString`, `JS_ToInt32`, `JS_GetPropertyStr` 等。
    *   **内存管理:** QuickJS 使用引用计数和垃圾回收。在 C API 层面，你需要正确管理 `JSValue` 的引用计数 (`JS_DupValue`, `JS_FreeValue`)，以防止内存泄漏或悬空指针。
    *   **错误处理:** C 代码需要检查 JS 执行后是否有异常 (`JS_IsException`, `JS_GetException`) 并妥善处理。

2.  **使用 `qjsc` 编译器:**
    *   **编译 JS 到可执行文件:** `qjsc` 可以将 JavaScript 文件（或多个文件，包括 ES6 模块）编译成一个独立的可执行二进制文件。这使得分发 JS 应用变得简单，用户无需安装 JS 运行时。
        ```bash
        qjsc -o myapp myscript.js mymodule.js
        ./myapp
        ```
    *   **编译 JS 到 C 代码 (字节码嵌入):** `qjsc -c -o output.c input.js` 会生成一个 C 文件，其中包含了 `input.js` 的字节码。你可以将这个 C 文件编译到你的 C/C++项目中，然后通过 QuickJS 的 C API 加载并执行这个字节码。这对于保护源码或减少启动时的解析时间很有用。
    *   **创建动态库/共享对象:** 可以将 JS 编译成 `.so` 或 `.dll` 文件，供其他程序加载。

3.  **C 模块 (Native Modules):**
    *   你可以用 C 编写模块，然后在 JavaScript 中通过 `import` 导入它们。
    *   模块需要一个初始化函数，例如 `js_init_module_mymath(JSContext *ctx, JSModuleDef *m)`。
    *   在这个函数中，你可以使用 `JS_SetModuleExport` 来导出 C 函数或 JS 值。
    *   这使得你可以用 C 实现性能关键部分或访问 JS 本身无法访问的系统功能，并以模块化的方式提供给 JS。

4.  **BigInt 和 BigFloat 支持:**
    *   QuickJS 原生支持 `BigInt` (任意精度整数) 和 `BigDecimal`/`BigFloat` (任意精度浮点数，通过 `-fbigfloat` 编译选项启用)。
    *   这对于需要高精度计算的场景（如金融、科学计算）非常有用，避免了标准 JavaScript `Number` 类型的精度问题。

5.  **异步操作和 Promises:**
    *   QuickJS 支持 `Promise` 和 `async/await`。
    *   当嵌入 QuickJS 时，你需要自己驱动事件循环。通过 `JS_ExecutePendingJob` 来执行待处理的 Promise 回调。
    *   你可以结合 C 模块来实现自定义的异步 I/O 操作，例如封装非阻塞的网络请求或文件读写，并在完成后 resolve/reject 相应的 Promise。

6.  **自定义对象和类 (C API):**
    *   你可以通过 C API 创建具有特定行为的自定义 JS 对象。
    *   `JS_NewObjectClass` 定义一个新的 JS 类。
    *   可以为这个类定义 `finalizer` (当对象被 GC 回收时调用) 和 `gc_mark` (用于标记对象内部引用的其他 JSValue)。
    *   可以为对象设置 getter/setter 属性，这些属性可以调用 C 函数。

7.  **序列化和反序列化:**
    *   QuickJS 提供了 `JS_WriteObject` 和 `JS_ReadObject` 函数，可以将 JS 值序列化为二进制格式（类似于 BSON 或 MessagePack，但有其特定格式），也可以从二进制格式反序列化回 JS 值。
    *   这比 `JSON.stringify/parse` 更快且支持更多类型（如 `Date`, `RegExp`, `ArrayBuffer`, 甚至循环引用，通过特定标志）。

8.  **沙箱化和资源限制 (有限的):**
    *   虽然 QuickJS 本身没有提供完整的沙箱化机制，但通过谨慎地设计 C API 暴露给 JS 的功能，可以限制脚本的能力。
    *   `JS_SetMemoryLimit` 可以限制 JS 运行时使用的内存。
    *   `JS_SetMaxStackSize` 可以限制 JS 调用栈深度。
    *   可以中断长时间运行的脚本 (`JS_SetInterruptHandler`)。

9.  **调试支持 (有限的):**
    *   QuickJS 有一个基础的调试协议，但相比 V8 等引擎的调试工具链要简单很多。通常需要配合一些第三方工具或自行实现。

**高级用法场景举例:**

*   **轻量级物联网 (IoT) 设备:** 在资源受限的设备上运行 JS 逻辑。
*   **游戏脚本:** 用 JS 编写游戏逻辑、AI、UI 交互，而游戏引擎核心是 C/C++。
*   **服务器端应用:** 配合 C 编写的高性能网络库，用 JS 处理业务逻辑。
*   **CLI 工具:** 使用 `qjsc` 将 JS 工具编译成快速启动的本地可执行文件。
*   **WebAssembly (WASM) 运行时:** QuickJS 本身可以被编译成 WASM，在浏览器或 Node.js 中运行 JS。反过来，QuickJS 也可以加载和运行 WASM 模块（如果宿主环境或 C 模块提供了支持）。

掌握这些高级用法，特别是 C API，能让你最大限度地发挥 QuickJS 的潜力，将其集成到各种复杂的系统中。核心在于理解其 C API 的设计和 JS 引擎的内部工作方式。