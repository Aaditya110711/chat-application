// $("#attach").click(function () {
//   $(".attachement").toggle();
// });
$("#dset").click(function () {
  $(".setting-drop").toggle("1000");
});
$(document).ready(function(){
    $(".flip").click(function(){
        $(".message-box").show("slide", { direction: "right" }, 10000);
    });

    $("#back").click(function(){
        $(".message-box").hide("slide", { direction: "left" }, 10000);
    });
});