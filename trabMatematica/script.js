function appendValue(value) {
    document.getElementById("display").value += value;
}

function clearDisplay() {
    document.getElementById("display").value = '';
}

function calculate() {
    try {
        let result = eval(document.getElementById("display").value);
        document.getElementById("display").value = result;
    } catch (e) {
        document.getElementById("display").value = 'Erro';
    }
}

function adjustFontSize(action) {
    const display = document.getElementById("display");
    const header = document.querySelector("header h1");

    let displayFontSize = parseInt(window.getComputedStyle(display).fontSize);
    let headerFontSize = parseInt(window.getComputedStyle(header).fontSize);

    if (action === 'increase') {
        display.style.fontSize = (displayFontSize + 2) + 'px';
        header.style.fontSize = (headerFontSize + 2) + 'px';
    } else if (action === 'decrease') {
        display.style.fontSize = (displayFontSize - 2) + 'px';
        header.style.fontSize = (headerFontSize - 2) + 'px';
    }
}
