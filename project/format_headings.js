const fs = require('fs');
const filePath = 'C:/AIprojects/roaddata/hubei/release/project/20260808.html';
let content = fs.readFileSync(filePath, 'utf8');

content = content.replace(/<h4 class="text-base font-bold text-brand-800"/g, '<h4 class="text-base font-bold text-slate-800 mb-1"');

content = content.replace(/<h3 class="text-base font-bold text-slate-800">/g, '<h3 class="text-base font-bold text-slate-800 mb-1">');

content = content.replace(/<h2 class="text-lg font-bold text-slate-800 border-l-4 border-brand-600 pl-3">1\.3\.4\./g, '<h2 class="text-base font-bold text-slate-800 mb-1">1.3.4.');

content = content.replace(/<strong class="text-slate-800 block font-bold">1\.3\.4\./g, '<strong class="text-sm font-bold text-slate-700 block mb-1">1.3.4.');

content = content.replace(/<h3 class="font-bold text-slate-800 text-base">/g, '<h3 class="text-base font-bold text-slate-800 mb-1">');

content = content.replace(/<h3 class="font-bold text-slate-900 text-base flex items-center">/g, '<h3 class="text-base font-bold text-slate-800 flex items-center mb-1">');

content = content.replace(/<h3 class="text-base font-bold text-slate-800 flex items-center">/g, '<h3 class="text-base font-bold text-slate-800 flex items-center mb-1">');

content = content.replace(/<h3 class="font-bold text-slate-800 mb-1">/g, '<h3 class="text-base font-bold text-slate-800 mb-1">');

fs.writeFileSync(filePath, content, 'utf8');
console.log("Success");
