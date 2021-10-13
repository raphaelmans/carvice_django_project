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
        $('#modal_user_firstname').val(parsedRes.first_name)
        $('#modal_user_userid').val(parsedRes.user_id) 
        $('#modal_user_lastname').val(parsedRes.last_name)
        $('#modal_user_username').val(parsedRes.username)
        $('#modal_user_password').val(parsedRes.password)
        $('#modal_user_phone').val(parsedRes.phone_number)
        $('#modal_user_email').val(parsedRes.email_address)
    }
}

async function showBookingModal(booking_id){
    $("#viewBookingModal").modal('show')
    $("#modal_booking_bookingid").val(booking_id)

    const res = await fetch(`http://127.0.0.1:8000/api/bookingById?booking_id=${booking_id}`, {
    method: "GET",
    headers: {
        "Content-Type": "application/json",
        "X-CSRFToken": csrftoken ,
    },
    });
    console.log(res);

    const jsonString = await res.text()
    if(res.status === 200){
        const parsedRes = JSON.parse(jsonString) 
        $('#modal_booking_userid').val(parsedRes.user_id)
        $('#modal_booking_rentid').val(parsedRes.rent_id) 
        $('#modal_booking_pickuplocation').val(parsedRes.pickup_location)
        $('#modal_booking_dropofflocation').val(parsedRes.dropoff_location)
        $('#modal_booking_pickupdate').val(parsedRes.pickup_date)
        $('#modal_booking_dropoffdate').val(parsedRes.dropoff_date)
        $('#modal_booking_pickuptime').val(parsedRes.pickup_time)
        $('#modal_booking_dropofftime').val(parsedRes.dropoff_time)
    }
}

async function showAdminModal(id){
    $("#viewAdminModal").modal('show')
    $("#modal_admin_adminid").val(id)

    const res = await fetch(`http://127.0.0.1:8000/api/adminById?admin_id=${id}`, {
    method: "GET",
    headers: {
        "Content-Type": "application/json",
        "X-CSRFToken": csrftoken ,
    },
    });

    const jsonString = await res.text()
    if(res.status === 200){
        const parsedRes = JSON.parse(jsonString) 
        console.log(parsedRes)
        $("#modal_admin_adminid_select").val(parsedRes.admin_id).change();
        $("#modal_admin_userid").val(parsedRes.user_id).change();
    }
}

async function showBillModal(id){
    $("#viewBillModal").modal('show')
    $("#modal_bill_billno").val(id)

    const res = await fetch(`http://127.0.0.1:8000/api/billById?bill_no=${id}`, {
    method: "GET",
    headers: {
        "Content-Type": "application/json",
        "X-CSRFToken": csrftoken ,
    },
    });

    const jsonString = await res.text()
    if(res.status === 200){
        const parsedRes = JSON.parse(jsonString) 
        $("#modal_bill_bookingid").val(parsedRes.booking_id).change();
        $("#modal_bill_totalfee").val(parsedRes.total_fee).change();
    }
}

const dateForDateTimeInputValue = date => new Date(date.getTime()).toISOString().slice(0, 19)
async function showConfirmModal(bookId,adminId){
    $("#viewConfirmationModal").modal('show')
    $("#modal_confirm_bookingid").val(bookId)
    $("#modal_confirm_adminid").val(adminId)

    const res = await fetch(`http://127.0.0.1:8000/api/confirmById?booking_id=${bookId}&admin_id=${adminId}`, {
    method: "GET",
    headers: {
        "Content-Type": "application/json",
        "X-CSRFToken": csrftoken ,
    },
    });

    const jsonString = await res.text()
    if(res.status === 200){
        const parsedRes = JSON.parse(jsonString) 
        $("#modal_confirm_bookingid").val(parsedRes.booking_id).change();
        $("#modal_confirm_adminid").val(parsedRes.admin_id).change();
        $("#modal_confirm_date").val(dateForDateTimeInputValue(new Date(parsedRes.date)))
    }
}


async function openDeleteModal(id,model_type){  
    $("#deleteConfirmModal").modal('show')
    $("#delete_id").val(id)
    $("#delete_model_type").val(model_type)
}
