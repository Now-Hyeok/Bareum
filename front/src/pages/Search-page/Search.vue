<template lang="">
	<div class="background" style="display: flex; flex-direction:column; justify-content: center; align-items: center; padding-top: 63px;">
		<button class="search_option" @click="open_popup('personalize')">관심 분야로 검색</button>
		<button class="search_option" @click="open_popup('ingredient')">영양 성분으로 검색</button>
		<div v-if="popup" style="display: flex; flex-direction: column;">
			<customSearch :selected_option="selected_option" :popup="popup" @close_popup="(close_popup) => popup = close_popup" @selected_items="(option, item) => searchItems(option, item)" ></customSearch>
		</div>
	</div>
</template>

<script>
import { ref } from 'vue';
import { useRouter } from "vue-router";
import customSearch from '../../components/CustomSearch.vue';

export default {
	name: 'search',
	components:{ customSearch },
	emits: ['searchQuery'],
	setup(context) {
		const searchPlaceholder = ref('검색어를 입력해주세요');
		const router = useRouter()
		const popup = ref(false);
		const selected_option = ref(null);
		
		const open_popup = (params) => {
            if(popup.value == true & selected_option.value == params) {
				selected_option.value = null;
				popup.value = false;
			}
            
            else {
                selected_option.value = params;
				popup.value = true;
			}
		}
		
		const searchItems = (option, items) => {
			console.log(option, items);
			if(items.length != 0) {
				router.push({name: 'resultPage', query: { 'q': items.join(','), 'option': option }});
			}
		};

		return {
			searchPlaceholder,
			popup,
			selected_option,
			open_popup,
			searchItems,
		};
	}
}
</script>

<style>
.search_option {
	width: min(72vw, 66vh);
	margin: 2vh 0;
	border-radius: 10px;
	border: none;
	background-color: #2dce89;
	color: white;
	font-size: 1.1em;
	text-decoration: none;
	font-weight: 750;
}

</style>