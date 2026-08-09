const fs = require('fs');
const filePath = 'C:/AIprojects/roaddata/hubei/release/project/20260808.html';
let content = fs.readFileSync(filePath, 'utf8');

const oldHeader = '<h3 class="text-md font-bold text-slate-800 border-l-4 border-brand-600 pl-3">1.7.2. 项目验收成果表</h3>';
const newHeader = '<h3 class="font-bold text-slate-800 mb-1">1.7.2. 项目验收成果表</h3>';

content = content.replace(oldHeader, newHeader);

fs.writeFileSync(filePath, content, 'utf8');
console.log("Success");
