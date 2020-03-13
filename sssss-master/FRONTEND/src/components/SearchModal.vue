<template>
<!-- Modal -->
<div class="modal fade" id="searchModal" tabindex="-1" role="dialog" aria-labelledby="myModalLabel" aria-hidden="true">
	<div class="modal-dialog">
		<div class="modal-content">
			<div class="modal-header">
                <h4 class="modal-title" id="myModalLabel">Study 장소 검색하기</h4>
				<button type="button" class="close" data-dismiss="modal" aria-label="Close"><span aria-hidden="true">close&times;</span>
				</button>
			</div>
			<div class="modal-body">
                <input type="email" class="form-control" id="exampleInputEmail1" aria-describedby="emailHelp" placeholder="ex)스타벅스, 광주" v-model="searchkeyword.keywordname">
                <div class="form-check form-check-inline">
                    <input class="form-check-input" type="radio" name="radioLocationName" id="radioLocationName" value="장소명" v-model="searchkeyword.keywordtype">
                    <label class="form-check-label" for="radioLocationName">장소명</label>
                </div>
                <div class="form-check form-check-inline">
                    <input class="form-check-input" type="radio" name="radioRegionName" id="radioRegionName" value="지역명" v-model="searchkeyword.keywordtype">
                    <label class="form-check-label" for="radioRegionName">지역명</label>
                </div>
                <div>
                    <!-- <div class="btn-group-toggle" data-toggle="buttons"> -->
                    <label class="btn btn-outline-success">
                        <input type="checkbox" value="의자가 편한" v-model="searchkeyword.favoriteArr"> 의자가 편한
                    </label>
                    <label class="btn btn-outline-secondary">
                        <input type="checkbox" value="분위기가 좋은" v-model="searchkeyword.favoriteArr"> 분위기가 좋은
                    </label>
                    <label class="btn btn-outline-warning">
                        <input type="checkbox" value="콘센트가 많은" v-model="searchkeyword.favoriteArr"> 콘센트가 많은
                    </label>
                    <label class="btn btn-outline-info">
                        <input type="checkbox" value="디저트 종류가 많은" v-model="searchkeyword.favoriteArr"> 디저트 종류가 많은
                    </label>
                    <label class="btn btn-outline-secondary">
                        <input type="checkbox" value="1인 책상이 많은" v-model="searchkeyword.favoriteArr"> 1인 책상이 많은
                    </label>
                    <label class="btn btn-outline-success">
                        <input type="checkbox" value="목재 디자인" v-model="searchkeyword.favoriteArr"> 목재 디자인
                    </label>
                    <label class="btn btn-outline-warning">
                        <input type="checkbox" value="은은하고 아늑한" v-model="searchkeyword.favoriteArr"> 은은하고 아늑한
                    </label>
                    <label class="btn btn-outline-secondary">
                        <input type="checkbox" value="흡연실이 있는" v-model="searchkeyword.favoriteArr"> 흡연실이 있는
                    </label>
                    <!-- </div> -->
                </div>
            </div>
			<div class="modal-footer">
				<button type="button" class="btn btn-default" data-dismiss="modal">취소</button>
				<button type="button" class="btn btn-primary" @click="search()">검색</button>
			</div>
		</div>
	</div>
</div>
</template>

<script>
// window.csrf_token = "{{ csrf_token() }}"
import axios_common from '../axios_common.js'
import router from '../router/index.js'

export default {
    data: function() {
        return {
            searchkeyword : {
                keywordname : '',
                keywordtype : '',
                favoriteArr : []
            }
        }
    },
    methods: {
        search() {
            axios_common.post("/search/", this.searchkeyword)
            .then(res => {
                console.log(res)
                //router.push({name:'map', params: {chichi: 123}})
                // router.push({name:'map'})
                router.push('/map')
            })
            .catch((e)=>{
                console.log(e)
            })
        }
    }
}
</script>

<style>

</style>