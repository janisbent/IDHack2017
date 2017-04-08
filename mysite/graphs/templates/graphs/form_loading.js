var person_form = '<hr> <form id="person_form" method="post" action="javascript:display_data()">' +
        '<p>' +
            'Name: <input type="text" name="name" maxlength="30"/>' +
            '<div class="option-spacing"> </div>' +
            '<br> Personal Info: <br> <textarea id="bio" name="bio" rows="4" cols="60"> </textarea> ' +
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
            '<br> About this group: <br> <textarea id="bio" name="gbio" rows="4" cols="60"> </textarea>'+
            '<br>'+
            '<button>Add Group</button>'+
            '<br>'+
            '<button type="submit" value="OK" onclick="javascript:close_form()">Done Adding Groups </button>'+
            '<div id="groups"></div>'+
            '<hr>'+
        '</p>'+
    '</form>';

var relationship_form = '<form id="group_form" method="post" action="javascript:display_rel()">'+
        '<p>'+ 
            '<hr>'+
            'Who is this relationship between?'+
            '<div id="inhabitants"></div>'+
            '<br>'+
            'Notes: <br> <textarea id="bio" name="notes" rows="4" cols="60"> </textarea>'+
            '<br> <br>'+
            'What is the quality of this relationship? <br>'+
            '<input type="radio" name="quality" value="positive"> Positive </input>'+
            '<input type="radio" name="quality" value="neutral"> Neutral </input>'+
            '<input type="radio" name="quality" value="negative"> Negative </input>'+
            '<br> <br>'+
            'How strong is this relationship? <br>'+
            '<input type="range" name="strength" min="0" max="100">'+
            '<br>'+
            '<button>Add Relationship</button>'+
            '<br>'+
            '<button type="submit" value="OK" onclick="javascript:close_form()">Done entering relationships</button>'+
            '<hr>'+
        '</p>'+
    '</form>';

var graph_data = [];
var groups = [];
var people = [];
var relations = [];
var gchecks = "";
var options = "";


function display_rel(){
    var relstring = "Relationships:";
    newrel = add_rel();

    friendly = "<br>" + newrel.party1 + " and " + newrel.party2 + " have a " +
               newrel.quality + " relationship with strength " + newrel.strength;

    $("#rels").html($("#rels").html() + friendly);

}

function add_rel(){
    var party1 = $("#box1").val();
    var party2 = $("#box2").val();
    var quality = $("input[name='quality']:checked").val();
    var notes = $("#bio").val();
    var strength = $("input[name='strength'").val();

    var newrel = {"party1":party1, "party2":party2, "quality":quality,
                    "notes":notes, "strength":strength};
    relations.push();
    return newrel;

    update_server("/add_rel");
}

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
    var name = $("input[name='gname']").val();
    var bio = $("#bio").val();
    groups.push({"name": name, "bio": bio});

    options = options + "<option name='" + name + "'value='" + name + "'>" + name + "</option>";
    gchecks = gchecks + "<input type='checkbox' name='" + name +"'>" + name + "</input> <br>";

    update_server("/add_group"); 
}


function display_data() {
    var gender = $("input[name='gender']:checked").val();
    var age    = $("input[name='age']:checked").val();
    var name   = $("input[name='name']").val();
    var bio    = $("#bio").val();
    var inf    = $("input[name='influence']").val();
    var gps    = [];

    groups.map(function(g){
        if($("input[name='" + g.name + "']:checked").val() == "on"){
            gps.push(g.name);
        }
    });

    // keep options up to date
    options = options + "<option value='" + name + "'>" + name + "</option>";

    people.push({"name": name, "age": age, "gender":gender,
                 "influence": inf, "bio": bio, "groups": gps});

    var informative = name + ", " + gender + ", " + age + " influence: " + inf + "<br> Member of: " + gps;  
    var new_dataset = $('#dataset').html() + "<br>" + informative + "<br>";
    $('#dataset').html(new_dataset);

    close_form();

    $('#form').html(person_form);
    update_server("/add_person");
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

function update_server(url, data){
    $.post(url, data, function(){
        console.log("served " + data);
    })
}

$(document).ready(function(){
    $('#form').html(person_form);
    $('#form').hide();

    $("#person_enter").click(function(){
        open_form(person_form);
        $("#groups").html(gchecks);
    });

    $("#village_setup").click(function(){
        open_form(group_form);
    });

    $("#rel_add").click(function(){
        open_form(relationship_form);
        var box1 = "<select id='box1'>" + options + "</select>";
        var box2 = "<select id='box2'>" + options + "</select>";
        $("#inhabitants").html(box1 + " " + box2);
    });
});