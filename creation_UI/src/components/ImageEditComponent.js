
import '../App.css';
import React, {useState} from 'react';
import handImage from '../photos/Hands.jpg';
import handPain from '../photos/handPain.jpg';
import { useNavigate } from 'react-router-dom';
import finalImage from '../photos/handPainFinal.jpg';


function ImageEditComponent() {


    let navigate = useNavigate();

    const handleContinue = () => {
        navigate('/ImproveComponent'); // Use the path you've defined for ImproveComponent in your Router
    };

    let myNavigate = useNavigate();

    const myhandleContinue = () => {
        myNavigate('/')
    }



    return (
        <div>

            <p style={{color: 'black'}}>According to your input, we were able to curate this image.</p>
            <div className="photo-window" style={{marginLeft: '220px'}}>

                <img src={finalImage} alt={'Picture of hands'} className="photo-window img"/>
            </div>
            {/* Output of the final image according to user input.}

            {/*
            {/*For users who choose a photo from existing images.}
            <p style={{color: 'black'}}>How would you like to customize your photo?</p>
            <div className="container">

                <button type="button" className="btn btn-secondary" onClick={myhandleContinue}
                        style={{marginLeft: '700px'}}>Go Back
                </button>

            </div>


            <div className="photo-window" style={{marginLeft: '220px'}}>
                <img src={handImage} alt={'Picture of hands'} className="photo-window img"/>
            </div>

            <div className="button-container">
                <p style={{color: 'black'}}>Increase the picture sharpness by 10%.</p>

            </div>

            <div className="container">

                <button type="button" className="btn btn-secondary" onClick={handleContinue}
                        style={{marginTop: '20px', marginLeft: '700px'}}>Continue
                </button>

            </div>
            */}


            {/*
            {/* For users who want to generate images using a prompt}
            <p style={{color: 'black'}}>How would you like to customize it further?</p>
            <div className="container">

                <button type="button" className="btn btn-secondary" onClick={myhandleContinue}
                        style={{marginLeft: '700px'}}>Go Back
                </button>

            </div>
            <div className="photo-window" style={{marginLeft: '220px'}}>

                <p style={{marginTop: '120px', color: 'black'}}>Increase the sharpness of the picture by 10%</p>
            </div>
            <div className="container">

                <button type="button" className="btn btn-secondary" onClick={handleContinue}
                        style={{marginTop: '100px', marginLeft: '700px'}}>Continue
                </button>

            </div>
            */}

            {/*
            {/* The main page}
            <p style={{color: 'black'}}> Welcome to the Chronic Pain Customizer! How do you want to visualize your pain?</p>
            <div className="container">
                <div className="photo-window">

                    <p style={{marginTop: '120px', color: 'black'}}>Provide a picture of a hand</p>
                </div>
                <div className="photo-window">
                    <img src={handImage} alt={'Picture of hands'} className="photo-window img"/>
                </div>

            </div>
            */}
            {/*


            <div className="button-container">
                <p style={{color: 'black'}}>Create Your Own Image using prompt</p>
                <button type="button" className="btn btn-secondary" style={{marginRight: '35px'}}>Choose From Existing
                    Images
                </button>
            </div>
            <div className="container">

                <button type="button" className="btn btn-secondary" onClick={handleContinue}
                        style={{marginTop: '100px', marginLeft: '700px'}}>Continue
                </button>

            </div>
            */}
        </div>
    );
}

export default ImageEditComponent;