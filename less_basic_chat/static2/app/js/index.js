var messages = [];

function getChats(){
  $.ajax({
    url: '/api/v1/messages',
    type: "GET",
    async: false,
    success: function(data){
      messages = data;
    },
    error: function(err){
      console.log(err);
    },
    complete: function(data){
      console.log("Messages received");
    }
  });
}

function appendChats(){
  for (var i = 0; i < messages.length; i++) {
    $('#messages').append(`<li>${messages[i].username} - ${messages[i].message}</li>`)
  }
}

function appendNewChats(){
  var newUser = $("#id_username").val();
  var newMessage = $("#id_message").val();

  postChat(newUser, newMessage);
  $('#messages').append(`<li>${newUser} - ${newMessage}</li>`)
}

function postChat(newUser, newMessage){
  var roomId = window.location.href.split("/").slice(-1).pop();
  ajaxSetup();

  $.ajax({
    url: "/api/v1/messages",
    type: "POST",
    data: {
      room: roomId,
      username: newUser,
      message: newMessage,
    },
    async: false,
    success: function(data){
      console.log("success");
    },
    error: function(data){
      console.log("fail");
    },
    complete: function(data){
      console.log("complete");
    }
  });
}

function ajaxSetup(){
  var csrftoken = Cookies.get('csrftoken');

  function csrfSafeMethod(method) {
    return (/^(GET|HEAD|OPTIONS|TRACE)$/.test(method));
  }

  $.ajaxSetup({
    beforeSend: function(xhr, settings) {
      if (!csrfSafeMethod(settings.type) && !this.crossDomain) {
        xhr.setRequestHeader("X-CSRFToken", csrftoken);
        }
    }
  });
}

$(document).ready(() => {
  getChats();
  appendChats();

  $("#submit-message").on("click", (e) => {
    e.preventDefault();
    appendNewChats();
  })

})
