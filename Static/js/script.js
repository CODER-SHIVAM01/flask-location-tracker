// function testclick(){
//     alert("js connected");
// }
// function jsclick(){
//     console.log("working backed");
// }

// function sendData(){
//     fetch("/collect",{
//         method:"Post",
//         headers:{
//             "content-type":"application/json"
//         },
//         body:JSON.stringify({
//             "Name":"Shivam",
//             "Aim":'Data Analyst',
//             "Mother Name":"Reena Jaiswal"
//         })
//     })
//     .then(Res=> Res.json())
//     .then(data=>{
//         console.log("Server Response :", data);
//         alert("Data Sent Successfully")
//     });
// }

function getLoc(){
    if(!navigator.geolocation){
        alert("Geolocation is not Suportted");
        return;
    }
navigator.geolocation.getCurrentPosition(
    success,
    error,

     {
        enableHighAccuracy: true,
        timeout: 10000,
        maximumAge: 0
    }
    );

}

function success(position){
    const latitude=position.coords.latitude;
    const longitude=position.coords.longitude;

    document.getElementById("address").innerText="Fetching address..."


    console.log("Latitude:" ,latitude);
    console.log("Longitude:", longitude);

    // Google Maps Link
    // const mapLink=`https://www.google.com/maps?q=${latitude},${longitude}`;
    // console.log("Map :",mapLink);
    
    fetch("/collect",{
        method:"POST",
        headers:{
            "Content-Type": "application/json"

        },
        body:JSON.stringify({
            lat:latitude,
            lon:longitude,
            // map:mapLink

        })
    })

    .then(res => {
    if (!res.ok) {
        throw new Error("Server error");
    }
    return res.json();
})

    // .then(res=>res.json())
    .then(data=>{
    console.log("Server response:", data);
    document.getElementById("address").innerText=data.address;
        // console.log(data)
        // alert("Location sent...");
        // window.open(mapLink);
        // const mapUrl =
        //     `https://www.google.com/maps?q=${latitude},${longitude}&output=embed`;

        // const map = document.getElementById("map");
        // map.src = mapUrl;
        // map.style.display = "block";
    })
    .catch(()=>{
    document.getElementById("address").innerText="Failed to fetch address";
    });
}

function error(err){
    console.error(err);
    alert("Location permission Denied");
}