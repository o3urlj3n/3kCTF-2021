// https://www.php.net/manual/en/indexes.functions.php
var banned = ['abs', 'sin', /* ... */]
Array.from(document.querySelectorAll('ul.gen-index.index-for-refentry ul>li'))
    .filter(e => !banned.includes(
        e.querySelector('.index').innerText)
    ).map(e => e.innerText).join('\n')
