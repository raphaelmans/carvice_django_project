async function handleUserModal(user_id){
    const res = await fetch(`http://127.0.0.1:8000/api/userById?user_id=${user_id}`, {
    method: "GET",
    headers: {
        "Content-Type": "application/json",
        "X-CSRFToken": csrftoken ,
    },
    });

    //json
    //fetch api
    //optional: asynchronous javascript

    const jsonString = await res.text()
    if(res.status === 200){
        const parsedRes = JSON.parse(jsonString) 
        $('#modal_user_firstname').val(parsedRes.first_name) // jquery
        $('#modal_user_userid').val(parsedRes.user_id) 
        $('#modal_user_lastname').val(parsedRes.last_name)
        $('#modal_user_username').val(parsedRes.username)
        $('#modal_user_password').val(parsedRes.password)
    }
}
