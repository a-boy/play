A **DLL (Dynamic Link Library)** is a shared library in Windows that contains code, data, and resources that multiple programs can use simultaneously. Unlike static libraries (which are linked at compile time), DLLs are loaded **dynamically at runtime**, allowing for modularity, reduced memory usage, and easier updates.

---

### **How DLLs Work (Step-by-Step)**
#### **1. Creation & Compilation**
- A DLL is written in C/C++ (or other languages) and compiled into a `.dll` file.
- It exports **functions, classes, or variables** that other programs can use.
- Example (C++):
  ```cpp
  // mylib.cpp
  extern "C" __declspec(dllexport) int add(int a, int b) {
      return a + b;
  }
  ```
  Compiled with:
  ```sh
  cl /LD mylib.cpp  # Creates mylib.dll and mylib.lib (import library)
  ```

#### **2. Exporting Functions**
- **`__declspec(dllexport)`** marks functions for export.
- **DEF files** can also define exports (alternative method).

#### **3. Using a DLL (Linking)**
A program can use a DLL in **two ways**:
##### **A. Load-Time Dynamic Linking (Implicit Linking)**
- The program links to an **import library (`.lib`)** at compile time.
- The OS loader automatically loads the DLL when the program starts.
- Example (C++):
  ```cpp
  // main.cpp (links with mylib.lib)
  #include <windows.h>
  extern "C" __declspec(dllimport) int add(int a, int b);

  int main() {
      int result = add(2, 3); // DLL loaded automatically
      return 0;
  }
  ```
  - **Pros**: Simple, no manual loading.
  - **Cons**: If DLL is missing, the program won't start.

##### **B. Run-Time Dynamic Linking (Explicit Linking)**
- The program manually loads the DLL and resolves functions at runtime.
- Uses **`LoadLibrary()`**, **`GetProcAddress()`**, and **`FreeLibrary()`**.
- Example (C++):
  ```cpp
  // main.cpp (no import library needed)
  #include <windows.h>

  typedef int (*AddFunc)(int, int);

  int main() {
      HMODULE hDll = LoadLibrary(TEXT("mylib.dll"));
      if (hDll) {
          AddFunc add = (AddFunc)GetProcAddress(hDll, "add");
          if (add) {
              int result = add(2, 3); // Call DLL function
          }
          FreeLibrary(hDll); // Unload when done
      }
      return 0;
  }
  ```
  - **Pros**: More control (e.g., optional DLLs, delayed loading).
  - **Cons**: More complex, error-prone if function is missing.

#### **4. Loading & Execution**
- The **Windows Loader** loads the DLL into memory when:
  - The program starts (for load-time linking).
  - `LoadLibrary()` is called (for run-time linking).
- The DLL's **`DllMain()`** function (if present) is called:
  ```cpp
  BOOL APIENTRY DllMain(HMODULE hModule, DWORD ul_reason, LPVOID lpReserved) {
      switch (ul_reason) {
          case DLL_PROCESS_ATTACH: // Called when loaded
          case DLL_THREAD_ATTACH:  // Called for new threads
          case DLL_PROCESS_DETACH: // Called when unloaded
          case DLL_THREAD_DETACH:
      }
      return TRUE;
  }
  ```
- The program resolves function addresses (either implicitly via the import table or explicitly via `GetProcAddress`).

#### **5. Memory & Sharing**
- **Shared Code**: Multiple processes can share the **same DLL in memory** (reducing RAM usage).
- **Private Data**: Each process gets its own copy of global/static variables (unless explicitly shared via shared sections).

#### **6. Unloading**
- For **load-time linking**: DLL unloads when the process exits.
- For **run-time linking**: DLL unloads when `FreeLibrary()` is called (reference count reaches zero).

---

### **Key Concepts**
1. **Import Library (`.lib`)**
   - A stub file for load-time linking (contains function names and DLL references).
2. **Export Table**
   - Lists functions/variables the DLL exposes.
3. **Ordinal vs. Name Export**
   - Functions can be exported by **ordinal** (index) or **name** (preferred for readability).
4. **Delay-Load DLLs**
   - A