function checkBox(x) {
    let inputType = document.getElementById(x);
    if (inputType.type == 'password') {
        inputType.type = 'text';
    }else{
        inputType.type = 'password';
    }
}