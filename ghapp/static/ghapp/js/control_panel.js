
var url = "http://raspi/ghapp/commands/";

var lights_state = false;
$("#lights_button").click(function(){
    if (!lights_state){
    	$.post(url,{command:101},function(data, status){
    		alert(data);
    		$("#response_label").text(data);
    		lights_state = true;
    	});
    }else{
    	$.post(url,{command:100},function(data, status){
    		alert(data);
    		$("#response_label").text(data);
    		lights_state = false;
    	});
    }
});