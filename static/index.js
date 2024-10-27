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

function onTransferToCurrentAccount() {
    let amount = document.getElementById("transferAmount").value;
    postRequest("/api/transfermoneytocurrent", { amount: amount }, function(response) {
        console.log(response);
    });
    delayedRefresh();
}

function onTransferToSavingsAccount() {
    let amount = document.getElementById("transferAmount").value;
    postRequest("/api/transfermoneytocurrent", { amount: "-"+amount }, function(response) {
        console.log(response);
    });
    delayedRefresh();
}

function onTransferToGoal() {
    let amount = document.getElementById("transferAmount").value;
    postRequest("/api/transfermoneytogoal", { amount: amount }, function(response) {
        console.log(response);
    });
    delayedRefresh();
}

function onTakeLoan(){
    let amount = document.getElementById("transferAmount").value;
    postRequest("/api/takeloan", { amount: amount }, function(response) {
        console.log(response);
    });
    delayedRefresh();
}

var nextMonthUnixTimestamp = document.getElementById("countdowntext").innerText;
console.log(nextMonthUnixTimestamp);
nextMonthUnixTimestamp = parseInt(nextMonthUnixTimestamp);

function updateCountdown() {
    var now = Math.floor(Date.now() / 1000);
    var secondsLeft = nextMonthUnixTimestamp - now;
    document.getElementById("countdowntext").innerHTML = secondsLeft + " seconds until next month";
    document.getElementById("countdowntext").hidden = false;
    if (secondsLeft <= 0) {
        document.getElementById("countdowntext").innerHTML = "Loading next month...";
        document.getElementById("countdowntext").hidden = true;
        delayedRefresh();
    }
    // Update every half second
    setTimeout(updateCountdown, 1000);
}

updateCountdown();