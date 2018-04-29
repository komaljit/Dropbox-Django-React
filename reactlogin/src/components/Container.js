import React, {Component} from 'react';
import { Route, withRouter } from 'react-router-dom';
import * as API from '../api/API';
import '../Login.css';
import SignUp from "./SignUp";
import Login from "./Login";


class Container extends Component {
    state = {
        login: "SI",
        message: ''
    };

    login = (userdata) =>{
        console.log(userdata);
        console.log("passed details above");
        API.doLogin(userdata)
            .then((res)=>{
                if (res.status === 200){
                    localStorage.setItem("username", userdata.username );
                    console.log(localStorage.getItem('username'));
                    this.props.history.push("/files");
                }
                else if (res.status === 400){
                    this.setState({
                        message: "Wrong username or password. Try again..!!"
                    });
                }
            }).catch(error => {
            console.log(error);
            return error;
        });
    };

    loginOrSignup = (data) => {
        console.log(data);
        this.setState({
            message:'',
            login:data
        });
    };

    signUp = (userdata) =>{

        API.createUser(userdata)
            .then((status)  => {
                if (status === 201) {
                    this.setState({
                        message: "User details saved successfully!"
                    });
                } else if (status === 401){
                    this.setState({
                        message: "Email already exists!"
                    });
                }
            });
    };

    render() {
        return (
            <div className="container-fluid">
                { this.state.message===''?'':(
                    <div className="text-danger">
                        {this.state.message}
                    </div>)
                }


                <h1 className="text-center login-title"></h1>
                <div className="account-wall">
                    <div className="col-md-12">

                        {this.state.login === "SU" ?
                            <SignUp signUp={this.signUp} loginOrSignup={this.loginOrSignup}/>
                            :
                            <Login login={this.login} loginOrSignup={this.loginOrSignup}/>
                        }

                    </div>
                </div>
            </div>

        );
    }
}


export default withRouter(Container);