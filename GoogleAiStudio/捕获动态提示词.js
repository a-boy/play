(function() {
    // 创建一个全局可访问的对象来控制捕获器
    window.promptCatcher = {
        _observer: null,
        _collectedPrompts: new Set(),
        STORAGE_KEY: 'aiStudioDynamicPrompts',

        start: function() {
            // ==========================================================
            //  ↓ ↓ ↓  这行代码已经根据最新分析更新了 ↓ ↓ ↓
            // ==========================================================
            const placeholderSelector = 'p.input-rolling-placeholder';
            // ==========================================================

            const targetNode = document.querySelector(placeholderSelector);

            if (!targetNode) {
                console.error("错误：未能找到“伪占位符”元素。");
                console.error("请按照教程，使用“检查元素”功能找到动态变化的文本，并更新脚本中的 'placeholderSelector' 变量。");
                return;
            }
            
            // ... 后续代码与之前完全相同，无需修改 ...

            const storedData = localStorage.getItem(this.STORAGE_KEY);
            if (storedData) {
                try {
                    const parsedData = JSON.parse(storedData);
                    this._collectedPrompts = new Set(parsedData);
                    console.log(`已从 localStorage 加载了 ${this._collectedPrompts.size} 条已有的提示词。`);
                } catch (e) {
                    this._collectedPrompts = new Set();
                }
            }
            
            const mutationCallback = () => {
                const newPrompt = targetNode.innerText.trim();
                if (newPrompt && !this._collectedPrompts.has(newPrompt)) {
                    this._collectedPrompts.add(newPrompt);
                    console.log(`%c新提示词已捕获:`, 'color: green; font-weight: bold;', `"${newPrompt}"`);
                    this.saveToLocalStorage();
                }
            };

            this._observer = new MutationObserver(mutationCallback);
            const config = { childList: true, subtree: true, characterData: true };
            this._observer.observe(targetNode, config);
            
            const initialPrompt = targetNode.innerText.trim();
            if (initialPrompt && !this._collectedPrompts.has(initialPrompt)) {
                 this._collectedPrompts.add(initialPrompt);
                 this.saveToLocalStorage();
            }

            console.log("%c✅ 提示词捕获器已启动！", "color: blue; font-size: 16px;");
            console.log("正在监视元素:", targetNode);
            console.log("当您想停止时，请在控制台输入 'promptCatcher.stop()' 并按回车。");
        },

        stop: function() {
            if (this._observer) {
                this._observer.disconnect();
                this._observer = null;
                console.log("%c🛑 提示词捕获器已停止。", "color: red; font-size: 16px;");
                console.log(`总共捕获了 ${this._collectedPrompts.size} 条独特的提示词。`);
                console.table(Array.from(this._collectedPrompts));
            } else {
                console.warn("捕获器当前未运行。");
            }
        },

        saveToLocalStorage: function() {
            const promptsArray = Array.from(this._collectedPrompts);
            localStorage.setItem(this.STORAGE_KEY, JSON.stringify(promptsArray, null, 2));
            console.log(`已将 ${promptsArray.length} 条提示词保存到 localStorage。`);
        }
    };

    console.log("提示词捕获工具已加载。");
    console.log("请在控制台输入 'promptCatcher.start()' 并按回车来开始捕获。");

})();


/***
0
: 
"'Item: Apple, Price: $1'. Extract name, price to JSON.\nkeyboard_tab"
1
: 
"Brainstorm 5 unique app ideas for sustainable living\nkeyboard_tab"
2
: 
"Generate a collection of elementary math worksheet for addition and subtraction of 2 digits.\nkeyboard_tab"
3
: 
"Generate Python code for a simple calculator app\nkeyboard_tab"
4
: 
"Teach me a lesson on quadratic equations. Assume I know absolutely nothing about it.\nkeyboard_tab"
5
: 
"Generate a scavenger hunt for street food around the city of Seoul, Korea.\nkeyboard_tab"
***/