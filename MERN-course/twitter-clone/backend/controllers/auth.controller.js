import { generateTokenAndSetCookie } from "../lib/utils/generateTokenAndSetCookie.js";
import User from "../models/user.model.js";
import bcrypt from "bcryptjs";

export const signup = async (req, res) => {
    try {
        const { username, fullName, password, email } = req.body;
        const emailRegex = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
        if (!emailRegex.test(email)) {
            return res.status(400).json({ message: "Invalid email format" });
        }
        const existingUser = await User.findOne({username})
        if (existingUser) {
            return res.status(400).json({ message: "Username already exists" });
        }
        const existingEmail = await User.findOne({email})
        if (existingEmail) {
            return res.status(400).json({ message: "Email already exists" });
        }   
        const salt = await bcrypt.genSalt(10);
        const hashedPassword = await bcrypt.hash(password, salt);
        const newUser = new User({
            username,
            fullName,
            password: hashedPassword,
            email
        });
        if (newUser) {
            generateTokenAndSetCookie(newUser._id,res)
            await newUser.save();
            res.status(201).json({
                _id: newUser._id,
                username: newUser.username,
                fullName: newUser.fullName,
                email: newUser.email,
                profileImg: newUser.profileImg,
                coverImg: newUser.coverImg,
                bio: newUser.bio,
                link: newUser.link,
                followers: newUser.followers,
                following: newUser.following,
            });
        } else {
            res.status(400).json({ message: "User creation failed"  });
        }
    } catch (error) {
        res.status(500).json({ message: "Server error", error: error.message });
    }
}

export const login =  async (req, res) => {
    try {
        const {username,password} = req.body
        const user = await User.findOne({username})
        const isPasswordCorrect = await bcrypt.compare(password,user?.password || "")
        if ((!user) || (!isPasswordCorrect)) {
            return res.status(400).json({message:"invalid credentials during login"})
        }

        generateTokenAndSetCookie(user._id,res)

        res.status(200).json({
           _id: user._id,
            username: user.username,
            fullName: user.fullName,
            email: user.email,
            profileImg: user.profileImg,
            coverImg: user.coverImg,
            bio: user.bio,
            link: user.link,
            followers: user.followers,
            following: user.following, 
        })


    } catch (error) {
        res.status(500).json({ message: "Server error", error: error.message });
    }
}

export const logout = (req, res) => {
    try {
        res.cookie("jwt",'',{maxAge:0})
        res.status(200).json({message:"loggout"})
    } catch (error) {
        console.log("error logging out")
        res.status(500).json({error:"internal server error"})
    }
}

export const getMe = async (req,res)=> {
    try {
        const user = req.user;
        if (!user) {
            return res.status(404).json({ message: "User not found" });
        }
        res.status(200).json(user);
    } catch (error) {
        console.log("error in getMe controller", error.message)
        return res.status(500).json({message:"Internal Server Error"})
    }
}
         

export const getUsers = async (req, res) => {
    const response = await User.find({})
    res.status(200).json(response);
}