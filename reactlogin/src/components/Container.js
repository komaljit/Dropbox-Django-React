import React, {Component} from 'react';
import { withRouter } from 'react-router-dom';
import * as API from '../api/API';
import '../Login.css';
import SignUp from "./SignUp";
import Login from "./Login";
import TextField from 'material-ui/TextField';

// Container component that has Login and Signup as child components
class Container extends Component {
    state = {
        login: "SI",
        message: ''
    };

    // function which calls login API when user submits credentials
    login = (userdata) =>{
        console.log(userdata);
        console.log("passed details above");
        API.doLogin(userdata)
            .then((res)=>{
                if (res.status === 200){
                    localStorage.setItem("username", userdata.username );
                    console.log(localStorage.getItem('username'));
                    // this.props.history.push("/files");
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

    // function to switch view from login to sign-up and vice-versa
    loginOrSignup = (data) => {
        console.log(data);
        this.setState({
            message:'',
            login:data
        });
    };

    // function to call sing-up API
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

    componentWillMount(){
        if (localStorage.getItem('username')){
            console.log('route path changed to /files');
            this.props.history.push('/files');
        }
    }

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
                <div>
                    <div className="jumbotron">

                        <div className="row justify-content-md-center">
                            <TextField type="file" name="mypic" onChange={this.handleFileUpload}/>
                        </div>
                        <br/><br/>
                        <div className="container-fluid">
                            <div className="row">
                                <div className="col-sm-7 ">
                                    <a href="#" className="link-title " onClick={() => this.setState({
                                        fileparent:'',
                                        message:''
                                    })}>
                                        Dropbox
                                    </a>
                                </div>
                            </div>
                        </div>
                    </div>
                </div>
            </div>

        );
    }
}


export default withRouter(Container);