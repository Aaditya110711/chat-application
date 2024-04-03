$("#dset").click(function () {
  $(".setting-drop").toggle("1000");
});
$(window).on("load", function () {
  document.querySelector('#text_msgg').value = '';

});


// $("#send_messageForm").submit(function (e) {
//   e.preventDefault();
//   var csrftoken = $("[name=csrfmiddlewaretoken]").val();

//   console.log("object:::::::::::::;");

//   let formData = {
//   };
//   url = "http://127.0.0.1:8000/chats/send_msg";
//   $.ajax({
//     headers: { "X-CSRFToken": csrftoken },
//     type: "POST",
//     url: url,
//     data: formData,
//     dataType: "json",
//     encode: true,
//   })
//     .done(function (data) {
//       console.log(data);
//     })
//     .fail(function (error) {
//       console.log(error);
//     });
// });
