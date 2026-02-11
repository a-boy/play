import { genkit } from 'genkit';
import { googleAI } from '@genkit-ai/google-genai';

const ai = genkit({ plugins: [googleAI()] });
let q= 'Genkit有哪些成功使用案例，给出几个url';
//'Genkit如何生成mp3音乐？给出代码构架示例';
//'怎样用Genkit生成midi音乐？给出代码示例';
    //'How to use Genkit?';
    'Why is Genkit awesome?';

const { text } = await ai.generate({
    model: googleAI.model('gemini-3-flash-preview'),
    prompt: q
});
console.log('\n## '+q+'\n');
console.log(text);