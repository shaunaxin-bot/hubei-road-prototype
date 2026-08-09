const fs = require('fs');
const filePath = 'C:/AIprojects/roaddata/hubei/release/project/20260808.html';
let content = fs.readFileSync(filePath, 'utf8');

// 1. Fix 1.2.x (currently h4 text-brand-800 -> h3 text-slate-800)
content = content.replace(/<h4 class="text-base font-bold text-brand-800">(1\.2\.\d.*?)<\/h4>/g, '<h3 class="text-base font-bold text-slate-800 mb-2"></h3>');

// 2. Fix 1.3.1, 1.3.2 (currently h3 text-slate-800 without mb-2)
content = content.replace(/<h3 class="text-base font-bold text-slate-800">(1\.3\.[12]\..*?)<\/h3>/g, '<h3 class="text-base font-bold text-slate-800 mb-2"></h3>');

// 3. Fix 1.3.3 (has flex items-center)
content = content.replace(/<h3 class="text-base font-bold text-slate-800 flex items-center">(1\.3\.3\..*?)<\/h3>/g, '<h3 class="text-base font-bold text-slate-800 flex items-center mb-2"></h3>');

// 4. Fix 1.3.4 (currently h2 border-l-4 -> h3 text-slate-800)
content = content.replace(/<h2 class="text-lg font-bold text-slate-800 border-l-4 border-brand-600 pl-3">(1\.3\.4\..*?)<\/h2>/g, '<h3 class="text-base font-bold text-slate-800 mb-2"></h3>');

// 5. Fix 1.3.4.1 to 1.3.4.4 (currently strong -> h4)
content = content.replace(/<strong class="text-slate-800 block font-bold">(1\.3\.4\.\d\..*?)<\/strong>/g, '<h4 class="text-base font-bold text-slate-700 mb-1"></h4>');

// 6. Fix 1.7.1 and 1.7.2 (currently h3 without text-base)
content = content.replace(/<h3 class="font-bold text-slate-800 mb-1">(1\.7\.\d.*?)<\/h3>/g, '<h3 class="text-base font-bold text-slate-800 mb-2"></h3>');

// 7. Fix doc2 H3s: （一）, （二） etc.
content = content.replace(/<h3 class="font-bold text-slate-800 text-base">/g, '<h3 class="text-base font-bold text-slate-800 mb-2">');

// 8. Fix doc2 H3s with flex items-center (e.g. 1. 启动攻坚期)
content = content.replace(/<h3 class="font-bold text-slate-900 text-base flex items-center">/g, '<h3 class="text-base font-bold text-slate-800 flex items-center mb-2">');

fs.writeFileSync(filePath, content, 'utf8');
console.log("Success");
