function postRequest(url, data, callback) {
    var xhr = new XMLHttpRequest();
    xhr.open("POST", url, true);
    xhr.setRequestHeader("Content-Type", "application/json");
    xhr.onreadystatechange = function() {
        if (xhr.readyState === 4 && xhr.status === 200) {
            callback(xhr.responseText);
        }
    };
    xhr.send(JSON.stringify(data));
}

function delayedRefresh() {
    setTimeout(function() {
        window.location.reload();
    }, 1000);
}

function onBuyShare(shareName, sharePrice) {
    postRequest("/api/buyshare", { name: shareName, price: sharePrice }, function(response) {
        console.log(response);
    });
    delayedRefresh();
}

function onSellShare(shareName, sharePrice) {
    postRequest("/api/sellshare", { name: shareName, price: sharePrice }, function(response) {
        console.log(response);
    });
    delayedRefresh();
}