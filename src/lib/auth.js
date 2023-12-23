import { getAuth } from "@firebase/auth"
import { initializeApp } from "@firebase/app"

const firebase_cfg = {

    apiKey: "AIzaSyAuDjZDvMIM1Q0va7zHkWRCsmc998Z5CW8",
  
    authDomain: "authenthication-2ba09.firebaseapp.com",
  
    projectId: "authenthication-2ba09",
  
    storageBucket: "authenthication-2ba09.appspot.com",
  
    messagingSenderId: "932669762813",
  
    appId: "1:932669762813:web:e9a5129528c38d160e2294",
  
    measurementId: "G-DT82KDZ5TF"
  
  };

const firebase_app = initializeApp(firebase_cfg)

const firebase_auth = getAuth(firebase_app)
export default firebase_auth