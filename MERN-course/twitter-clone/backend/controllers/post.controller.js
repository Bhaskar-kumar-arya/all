import test from "node:test";
import Post from "../models/post.model.js";
import { v2 as cloudinary } from "cloudinary";
import { Notification } from "../models/notification.model.js";
import User from "../models/user.model.js";
import path from "path";

export const getAll = async (req, res) => {
    try {
        const posts = await Post.find({}).populate({
            path : 'user',
            select : '-password'
        }).populate({
            path : 'comments.user',
            select : '-password'
        })
        res.status(200).json(posts)
    } catch (error) {
        console.error("Error fetching posts:", error.message);
        res.status(500).json({ message: "Internal Server Error" });
    }
};

export const createPost = async (req, res) => {
  try {
    const { text } = req.body;
    let { img } = req.body;
    const userId = req.user._id.toString();
    if (!text && !img) {
      return res.status(400).json({ message: "Post content cannot be empty" });
    }
    if (img) {
      const uploadResponse = await cloudinary.uploader.upload(img);
      img = uploadResponse.secure_url;
    }
    const newPost = new Post({ text, img, user: userId });
    await newPost.save();
    return res
      .status(201)
      .json({ message: "Post created successfully", post: newPost });
  } catch (error) {
    console.error("Error creating post:", error.message);
    return res.status(500).json({ message: "Internal Server Error" });
  }
};

export const deletePost = async (req, res) => {
  try {
    const post = await Post.findById(req.params.id);
    if (!post) {
      return res.status(404).json({ message: "Post not found" });
    }
    if (post.user.toString() !== req.user._id.toString()) {
      return res
        .status(403)
        .json({ message: "Not authorized to delete this post" });
    }
    if (post.img) {
      const publicId = post.img.split("/").pop().split(".")[0];
      await cloudinary.uploader.destroy(publicId);
    }
    await Post.findByIdAndDelete(req.params.id);
    return res.status(200).json({ message: "Post deleted successfully" });
  } catch (error) {
    console.error("Error deleting post:", error.message);
    return res.status(500).json({ message: "Internal Server Error" });
  }
};

export const likeUnlikePost = async (req, res) => {
  try {
    const postId = req.params.id;
    const post = await Post.findById(postId);
    if (!post) {
      return res.status(404).json({ message: "Post not found" });
    }
    const userId = req.user._id.toString();
    const likeIndex = post.likes.indexOf(userId);
    if (likeIndex > -1) {
      post.likes.splice(likeIndex, 1);
      // Remove the user from likedPosts in User model
      await User.findByIdAndUpdate(req.user._id, {
        $pull: { likedPosts: postId }
      });
      await post.save();
    } else {
      post.likes.push(userId);
      // Add the user to likedPosts in User model
      await User.findByIdAndUpdate(req.user._id,{$push: {likedPosts : postId}})
      await post.save();
    }
    const notification = new Notification({
      from: req.user._id,
      to: post.user._id,
      type: "like",
    });
    await notification.save();
    return res
      .status(200)
      .json(post.likes);
  } catch (error) {
    console.error("Error liking/unliking post:", error.message);
    return res.status(500).json({ message: "Internal Server Error" });
  }
};

export const commentOnPost = async (req, res) => {
  try {
    const post = await Post.findById(req.params.id);
    const { text } = req.body;
    if (!text) {
      return res.status(400).json({ message: "Comment text cannot be empty" });
    }
    if (!post) {
      return res.status(404).json({ message: "Post not found" });
    }
    post.comments.push({
      text,
      user: req.user._id,
    });
    await post.save();
    return res
      .status(201)
      .json({ message: "Comment added successfully", post });
  } catch (error) {
    console.error("Error commenting on post:", error.message);
    return res.status(500).json({ message: "Internal Server Error" });
  }
};

export const getLikedPosts = async (req, res) => {
  const userId = req.params.id;
  try {
    const user = await User.findById(userId)
    if (!user) {
      return res.status(404).json({ message: "User not found" });
    }
    const likedPosts = await Post.find({_id: {$in : user.likedPosts}}).populate({
      path :'user',
      select : '-password'
    }).populate({
      path : "comments.user",
      select : '-password'
    })
    return res.status(200).json(likedPosts);
  } catch (error) {
    console.error("Error fetching liked posts:", error.message);
    return res.status(500).json({ message: "Internal Server Error" });
  }
}

export const getFollowingPosts = async (req,res) => {
  try {
    const user = await User.findById(req.user._id).populate('following');
    if (!user) {
      return res.status(404).json({ message: "User not found" });
    }
    const followingIds = user.following.map(following => following._id);
    const posts = await Post.find({ user: { $in: followingIds } })
      .populate({ path: 'user', select: '-password' })
      .populate({ path: 'comments.user', select: '-password' })
      .sort({ createdAt: -1 });
    return res.status(200).json(posts);
  } catch (error) {
    console.error("Error fetching following posts:", error.message);
    return res.status(500).json({ message: "Internal Server Error" });
  }
}

export const getUserPosts = async (req,res) => {
  try {
    const {username} = req.params
    const user = await User.findOne({username})
    if (!user) {
      return res.status(404).json({ message: "User not found" });
    }
    const posts = await Post.find({user : user._id}).populate({
      path : 'user' ,
      select : '-password'
    }).populate({
      path : 'comments.user' ,
      select : '-password'
    })
    return res.status(200).json(posts);
  } catch (error) {
    console.error("Error fetching user posts:", error.message);
    return res.status(500).json({ message: "Internal Server Error" });
  }
}