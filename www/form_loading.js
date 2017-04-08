var person_form = '<hr> <form id="person_form" method="post" action="javascript:display_data()">' +
        '<p>' +
            'Name: <input type="text" name="name" maxlength="30"/>' +
            '<div class="option-spacing"> </div>' +
            '<br> Personal Info: <br> <textarea name="bio" rows="4" cols="60"> </textarea> ' +
            '<br>            ' +
            '<br> Gender: ' +
            '<br> <input type="radio" name="gender" id="genderm" value="Male"> M </input> ' +
                 '<input type="radio" name="gender" id="genderf" value="Female"> F </input> ' +
            '<br> ' +
            '<br> Age: ' +
            '<br> <input type="radio" name="age" value="child"> Child </input> ' +
            '     <input type="radio" name="age" value="teen"> Teenager </input> ' + 
            '     <input type="radio" name="age" value="young adult"> Young adult </input> ' + 
            '     <input type="radio" name="age" value="adult"> Adult </input> ' +
            '     <input type="radio" name="age" value="old"> Elder </input> ' +
            '<br> ' +
            '<br> How influential is this person? <br> ' +
            '<input type="range" name="influence"> ' +
            '<br> Groups: ' +
            '<div id="groups"> Set up village groups! </div> ' +
            '<div class="option-spacing"> </div> ' +
            '<br> ' +
            '<button id="submit" type="submit" value="OK">Submit</button> ' +
        '</p> ' +
    '</form> <hr>';

var group_form = '<form id="group_form" method="post" action="javascript:display_group()">' +
        '<p>' +
            '<hr>'+
            'Name: <input type="text" name="gname" maxlength="60"/> '+
            '<br> About this group: <br> <textarea name="gbio" rows="4" cols="60"> </textarea>'+
            '<br>'+
            '<button>Add Group</button>'+
            '<br>'+
            '<button type="submit" value="OK" onclick="javascript:close_form()">Done Adding Groups </button>'+
            '<div id="groups"></div>'+
            '<hr>'+
        '</p>'+
    '</form>';

var graph_data = [];
var groups = [];
var people = [];

function display_group(){
    add_group();
    var groupstring = "Groups:";

    groups.map(function(group){
        groupstring = groupstring + "<br>" + group.name;
    });

    $("#form").html(group_form);

    $("#groupdata").html(groupstring);
}

function add_group(){
    name = $("input[name='gname']").val();
    bio = $("input[name='gbio'").val();
    groups.push({"name": name, "bio": bio});
}

function display_data() {
    var gender = $("input[name='gender']:checked").val();
    var age    = $("input[name='age']:checked").val();
    var name   = $("input[name='name']").val();
    var bio    = $("input[name='bio']").val();
    var inf    = $("input[name='influence']").val();

    people.push({"name": name, "age": age, "gender":gender,
                 "influence": inf, "bio": bio});

    var informative = name + ", " + gender + ", " + age + " influence: " + inf;  
    var new_dataset = $('#dataset').html() + "<br>" + informative;
    $('#dataset').html(new_dataset);

    close_form();

    $('#form').html(person_form);
}


function close_form(form){
    $('#form').hide();
    $('.option').show();
}

function open_form(form){
    $('#form').html(form);
    $('#form').show();
    $('.option').hide();
}

$(document).ready(function(){
    $('#form').html(person_form);
    $('#form').hide();

    $("#person_enter").click(function(){
        open_form(person_form);
    });

    $("#village_setup").click(function(){
        open_form(group_form);
    })
});