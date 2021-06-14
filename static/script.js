function close(){
    fetch('/close')
}
window.onbeforeunload = close;