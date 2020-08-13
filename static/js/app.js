

function sendData() {

    //データ取得

    var ticket = $('input[name="ticket"]:checked').val();
    var gender = $('input[name="gender"]:checked').val();
    var age = $('input[name="age"]').val();
    var title = $('input[name="title"]').val();
    var sibsp = $('input[name="sibsp"]').val();
    var parch = $('input[name="parch"]').val();
    var fare = $('input[name="fare"]').val();
    var embarked = $('input[name="embarked"]:checked').val();

    $.ajax({
        type: "POST",
        url: "/",
        data: {
            "ticket": ticket,
            "gender": gender,
            "age": age,
            "title" : title,
            "sibsp": sibsp,
            "parch": parch,
            "fare": fare,
            "embarked": embarked,
        }
    })
    .then(
        function (data) {
            $('#answer').html('<span class="answer">'+data['result']+'</span>')
        },
        function (data) {
            alert("予測失敗")
        }
    );
  
 
}
