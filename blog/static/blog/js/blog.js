// blog
// 
$(document).ready(function(){
        $('[data-toggle="tooltip"]').tooltip(); 
        });

$('#popover').popover({ 
    html : true,
    title: function() {
      return $("#popover-head").html();
    },
    content: function() {
      return $("#popover-content").html();
    }
});