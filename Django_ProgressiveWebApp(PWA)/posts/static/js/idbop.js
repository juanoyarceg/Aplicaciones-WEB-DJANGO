var dbPromise = idb.open('feeds-db',5,function(upgradeDb){
	upgradeDb.createObjectStore('feeds',{keyPath:'pk'});
});

	//coleccionamos los ultimos posts del servidor
	fetch('http://127.0.0.1:8000/getdata').then(function(response){
		return response.json();
	}).then(function(jsondata){
		dbPromise.then(function(db){
			var tx = db.transaction('feeds','readwrite');
			var feedStore = tx.objectStore('feeds');
			for(var key in jsondata){
				if(jsondata.hasOwnProperty(key)){
					feedStore.put(jsondata[key]);
				}
			}
		});
	});

	var post = "";
	dbPromise.then(function(db){
		var tx = db.transaction('feeds','readonly');
		var feedStore = tx.objectStore('feeds');
		return feedStore.openCursor();
	}).then(function logItems(cursor){
		if(!cursor){
			document.getElementById('offlinedata').innerHTML=post;
			return;	
		}
		for (var field in cursor.value){
			if (field=='fields'){
				feedsData = cursor.value[field];
				for (var key in feedsData){
					if (key == 'titulo')
					{
						var titulo = '<h3>'+feedsData[key]+'</h3>';
					}
					if (key == 'autor')
					{
						var autor = feedsData[key];
					}
					if (key == 'contenido')
					{
						var contenido = '<p>'+feedsData[key]+'</p>';
					}
				}
				post=post+'<br>'+titulo+'<br>'+autor+'<br>'+contenido+'<br>';
			}
		}
		return cursor.continue().then(logItems);
	});


