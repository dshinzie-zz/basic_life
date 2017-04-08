var chats = [];

function getChats() {
  $.ajax({
    url: "/api/v1/chats",
    type: "GET",
    dataType: 'json',
    cache: false,
    async:false,
    success: function(data){
      chats = data;
    },
    error: function(error){
      console.log(error);
    },
    complete: function(data){
      console.log("Retrieved all chats:");
    }
  });
}

function appendChats(chats){
  for (var i = 0; i < chats.length; i++) {
    $("#chat-list").append(`<li>${chats[i].name} - ${chats[i].message} - ${chats[i].published_date}</li>`);
  }
}

function appendNewChat(){
  var newName = $("#id_name").val();
  var newMessage = $("#id_message").val();

  $("#chat-list").append(`<li>${newName} - ${newMessage} - "test"</li>`);
  postChat(newName, newMessage);
}

function postChat(newName, newMessage){
  ajaxSetup();

  $.ajax({
    url: "/api/v1/chats/new",
    type: "POST",
    data: {
      name: newName,
      message: newMessage
    },
    async:false,
    success: function(data){
      console.log("success");
    },
    error: function(error){
      console.log(error);
    },
    complete: function(data){
      console.log("Retrieved all chats:");
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
  appendChats(chats);

  $('#send-chat').on('click', (e) =>{
    e.preventDefault();
    appendNewChat();
  })

})
