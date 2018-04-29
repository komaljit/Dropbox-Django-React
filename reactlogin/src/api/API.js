const api = process.env.REACT_APP_CONTACTS_API_URL || 'http://localhost:8000/api';

const headers = {
    'Accept': 'application/json'
};


export const doLogin = (payload) =>
    fetch(`${api}/login`, {
        method: 'POST',
        headers: {
            ...headers,
            'Content-Type': 'application/json'
        },
        credentials:'include',
        body: JSON.stringify(payload),
        })
        .then(res => {
            return res
        }).catch(error => {
            console.log(error);
            // return error;
        });


export const createUser = (payload) =>
    fetch(`${api}/signup`, {
        method: 'POST',
        headers: {
            ...headers,
            'Content-Type': 'application/json'
        },
        body: JSON.stringify(payload),
    }).then(res => {
        return res.status;
    })
        .catch(error => {
            console.log("This is error");
            return error;
        });


export const getFile = (filedata) =>
    fetch(`${api}/files`,{
        method: 'GET',
        credentials:'include'
        }).then(res =>{
                return res;
        }).catch(error => {
            console.log("This is error.");
            return error;
        });


export const uploadFile = (payload) =>
    fetch(`${api}/file/upload/`, {
        method: 'POST',
        body: payload,
        credentials:'include'
    }).then(res => {
        return res.json();
    }).catch(error => {
        console.log("This is error");
        return error;
    });

export const getState = (email) =>
    fetch(`${api}/userdetails`, {
        method: 'GET',
        credentials:'include'
        }).then(res => {
            if (res.status === 200){
                console.log(res);
                return res.text();
            }
        }).catch(error => {
            console.log("This is error.");
            return error;
        });

export const updateUser = (data) =>
    fetch(`${api}/updateuser`, {
        method: 'POST',
        headers: {
            ...headers,
            'Content-Type': 'application/json'
        },
        body: JSON.stringify(data),
        credentials:'include'
    }).then(res => {
        return res.status;
    }).catch(error => {
        console.log("This is error");
        return error;
    });


export const logout = () =>
    fetch(`${api}/logout`, {
        method: 'POST',
        headers: {
            ...headers,
            'Content-Type': 'application/json'
        },
        credentials:'include'
    }).then(res => {
        return res.status;
    }).catch(error => {
        console.log("This is error");
        return error;
    });