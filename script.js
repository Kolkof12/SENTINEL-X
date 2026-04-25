function setTheme(color) {
    document.body.className = color + '-theme';
}

function claimDaily() {
    let points = parseInt(document.getElementById('points-count').innerText);
    points += 20;
    document.getElementById('points-count').innerText = points;
    alert("مبروك! حصلت على الهدية اليومية 🎁");
}

function changeLang(lang) {
    if(lang === 'en') {
        document.getElementById('main-html').dir = 'ltr';
        // هنا تضيف كود تبديل النصوص للإنجليزية
    } else {
        document.getElementById('main-html').dir = 'rtl';
    }
}
