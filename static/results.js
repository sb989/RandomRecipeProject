
    var obj = JSON.parse(txt);
    console.log(obj);
    for(var i=0; i<obj.length;i++)
    {
        var div = document.createElement("div");
        div.className = "search_results";
    	var e = document.createElement("a");
    	if ("index" in obj[i])
    	{
    	    e.href = "/load_local/"+obj[i].index
    	}
    	else
    	{
    	   e.href = "/load_online/"+obj[i].id
    	}
       
        
       
        
        var txt = document.createElement("div");
        txt.className = "search_results_txt";
        txt.innerHTML = obj[i].title;
        e.appendChild(txt);
        
        
         var img = document.createElement("img");
        img.src = obj[i].image
        img.className = "search_results_img";
        e.appendChild(img);
        
        div.appendChild(e)
        var results = document.getElementById("results");
    	results.appendChild(div);
    }
    
