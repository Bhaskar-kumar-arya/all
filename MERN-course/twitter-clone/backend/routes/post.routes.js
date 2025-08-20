import mongoose from "mongoose";
import {
  commentOnPost,
  createPost,
  deletePost,
  getAll,
  likeUnlikePost,
  getLikedPosts,
  getFollowingPosts,
  getUserPosts
} from "../controllers/post.controller.js";
import { protectRoute } from "../middleware/protectRoute.js";
import express from "express";

const router = express.Router();

router.get("/all", getAll);
router.get("/likes/:id",protectRoute,getLikedPosts);
router.get("/following",protectRoute,getFollowingPosts);
router.get('/user/:username',getUserPosts)
router.post("/create", protectRoute, createPost);
router.post("/like/:id", protectRoute, likeUnlikePost);
router.post("/comment/:id", protectRoute, commentOnPost);
router.delete("/:id", protectRoute, deletePost);

export default router;
