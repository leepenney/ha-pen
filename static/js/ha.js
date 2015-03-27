function listenerSetup() {
    var buttons = document.getElementById('buttons');
    var labels = buttons.getElementsByTagName('label');
    for (var i=0; i < labels.length; i++) {
        labels[i].onclick = function() {
            toggle_timer(this);
        }
    }
    add_timer_listeners();
    var add_but = document.getElementById('add_but');
    add_but.onclick = function() {
        add_timer(this);
    }
}

function add_timer_listeners() {
    var forms = document.getElementsByTagName('form');
    for (var i=0; i < forms.length; i++) {
        if (forms[i].elements['save']) {
            forms[i].elements['save'].onclick = function() {
                save_timer(this);
            }
        }
        if (forms[i].elements['del']) {
            forms[i].elements['del'].onclick = function() {
                del_timer(this);
            }
        }
    }
}

function toggle_timer(item) {
    var socket_name = item.getAttribute('for');
    var socket = socket_name.substr(socket_name.lastIndexOf('-')+1);
    var req = new XMLHttpRequest();
    req.open('get', window.location.pathname+'/toggle/'+socket, true);
    req.send();
    req.onreadystatechange=function(){
        if (req.readyState == 4 && req.status == 200){
            if (req.responseText.indexOf('all') > -1) {
                var checkboxes = document.getElementsByTagName('input');
                for (i = 0; i < checkboxes.length; i++) {
                    if (checkboxes[i].id.indexOf('all') == -1) {
                        checkboxes[i].checked = (req.responseText == 'all:on') ? true : false;
                    }
                }                            
            } else {
                document.getElementById(socket_name).checked = (req.responseText == 'on') ? true : false;
            }
        }
    }
    return false;
}

function save_timer(item) {
    var socket_name = item.getAttribute('id');
    var socket = socket_name.substr(socket_name.lastIndexOf('-')+1);
    var form_fields = document.getElementById('form-'+socket).elements;
    var params = '';
    for (var i=0; i<form_fields.length; i++) {
        if (form_fields[i].type == 'checkbox') {
            params += '&'+form_fields[i].name+'='+form_fields[i].checked;
        } else {
            params += '&'+form_fields[i].name+'='+encodeURIComponent(form_fields[i].value);
        }
    }
    params = params.substring(1);
    var req = new XMLHttpRequest();
    req.open('post', window.location.pathname+'/mod/'+socket, true);
    req.setRequestHeader('Content-type','application/x-www-form-urlencoded');
    req.send(params);
    req.onreadystatechange=function(){
        if (req.readyState == 4 && req.status == 200) {
            if (req.responseText == 'saved') {
                var save_button = document.getElementById('save-'+socket);
                save_button.value = 'Saved';
            }
        }
    }
    return false;
}

function add_timer(item) {
    var form_fields = document.getElementById('add-timer').elements;
    var params = '';
    for (var i=0; i<form_fields.length; i++) {
        if (form_fields[i].type == 'checkbox') {
            params += '&'+form_fields[i].name+'='+form_fields[i].checked;
        } else {
            params += '&'+form_fields[i].name+'='+encodeURIComponent(form_fields[i].value);
        }
    }
    params = params.substring(1);
    var req = new XMLHttpRequest();
    req.open('post', window.location.pathname+'/add/', true);
    req.setRequestHeader('Content-type','application/x-www-form-urlencoded');
    req.send(params);
    req.onreadystatechange=function(){
        if (req.readyState == 4 && req.status == 200) {
            if (req.responseText != 'failed') {
                var timer_section = document.getElementById('timers');
                timer_section.innerHTML = req.responseText;
                add_timer_listeners();
            }
        }
    }
    return false;
}

function del_timer(item) {
    var socket_name = item.getAttribute('id');
    var socket = socket_name.substr(socket_name.lastIndexOf('-')+1);
    var req = new XMLHttpRequest();
    req.open('get', window.location.pathname+'/del/'+socket, true);
    req.send();
    req.onreadystatechange=function(){
        if (req.readyState == 4 && req.status == 200) {
            if (req.responseText == 'saved') {
                var elem = document.getElementById('form-'+socket).parentNode;
                elem.remove();
            }
        }
    }
    return false;
}

function add_device(item) {
    var form_fields = document.getElementById('add_device').elements;
    var params = '';
    for (var i=0; i<form_fields.length; i++) {
        params += '&'+form_fields[i].name+'='+encodeURIComponent(form_fields[i].value);
    }
    params = params.substring(1);
    var req = new XMLHttpRequest();
    req.open('post', window.location.pathname+'/add/', true);
    req.setRequestHeader('Content-type','application/x-www-form-urlencoded');
    req.send(params);
    req.onreadystatechange=function(){
        if (req.readyState == 4 && req.status == 200) {
            if (req.responseText != 'failed') {
                var devices_list = document.getElementById('devices_list');
                var new_device = document.createElement('li');
                new_device.innerHTML = '<h3>'+form_fields['name'].value+'</h3>';
                devices_list.appendChild(new_device);
            }
        }
    }
    return false;
}
