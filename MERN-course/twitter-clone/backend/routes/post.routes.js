import mongoose from 'mongoose'
import { commentOnPost, createPost, deletePost, getPosts, likeUnlikePost } from '../controllers/post.controller.js'
import { protectRoute } from '../middleware/protectRoute.js'

const router = mongoose.Router()

router.get('/',getPosts)
router.post('/create',protectRoute,createPost)
router.post('/like/:id',protectRoute,likeUnlikePost)
router.post('/comment/:id',protectRoute,commentOnPost)
router.delete('/',protectRoute,deletePost)

export default router