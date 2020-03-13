<template>
	<div class="container">
		<div class="col-md-12">
			<div class="card mb-4 box-shadow">
				<h3>댓글 정보</h3>                
				<div class="card-body flex-column align-items-start">
					<div class="col-md-12 card box-shadow">
						<h6>작성자</h6>
						<hr>
						<h6>이러쿵저러쿵</h6>                        
					</div>
					<div class="col-md-12">
						<form action="/action_page.php">
							<div class="form-group">
							<label for="comment">Comment:</label>
							<textarea class="form-control" rows="5" id="comment" name="text"></textarea>
							</div>
							<button type="submit" class="btn btn-primary">Submit</button>
						</form>
					</div>
				</div>                    
			</div>
		</div>
	</div>
</template>


<script>
import axios from 'axios'
// import jwtDecode from 'jwt-decode'

export default {
  data: function() {
    return {
      user_id : this.$store.getters.loggedInUser.user_id,
		}
	},
  methods: {
    likeStatus(){
      const token = this.$store.getters.requestHeader.headers.Authorization
      const requestHeader = { 
        headers: {
          Authorization: token
        }
      }
      
			axios.get(`http://localhost:8000/api/v1/${this.place_id}/comment/`, requestHeader)
      .then((res)=>{
        console.log(res.data)
        // console.log(res.data)
      
      })
    },
}
}

</script>

<style scoped>

</style>
