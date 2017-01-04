
function loadElement(userid,problemid,el){
    $.ajax("getstatus/"+userid+"/"+problemid,
            {
                success:function (data){
                    el.innerHTML=data;
                }
            }
          );

}

function toggleStatus(userid,problemid){
    $.ajax("toggle/"+userid+"/"+problemid,
            {
                success: function(){
                    updateStatusElements(userid,problemid);
                }
            }
          );
}


function updateStatusElements(userid,problemid){
    var eList = $(".status-element");
    for (i=0;i<eList.length;i++){
        loadElement(userid,problemid,eList[i]);
    }
}
