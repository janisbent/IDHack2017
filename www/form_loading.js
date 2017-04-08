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

var graph_data = [];

function display_data() {
    var gender = $("input[name='gender']:checked").val();
    var age    = $("input[name='age']:checked").val();
    var name   = $("input[name='name']").val();
    var bio    = $("input[name='bio']").val();
    var inf    = $("input[name='influence']").val();

    var informative = name + ", " + gender + ", " + age + " influence: " + inf;  
    var new_dataset = $('#dataset').html() + "<br>" + informative;
    $('#dataset').html(new_dataset);

    $('#form').hide();
    $('.option').show();

    $('#form').html(person_form);
}

$(document).ready(function(){
    $('#form').html(person_form);
    $('#form').hide();
    $("#person_enter").click(function(){
        $('#form').show();
        $('.option').hide();
    });
});