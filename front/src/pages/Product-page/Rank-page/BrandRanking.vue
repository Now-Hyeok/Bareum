<template>
    <div class="background bg-whitesmoke" style="padding-top: 56px; min-height: 100%; padding-bottom: 60px;">

<div v-for="(brand,index) in brandRanking" :key="index" style="margin-bottom: 5%;">
    <div style="background-color: white; border:none;">업체명 : {{ brand.brand }}</div>
    <div class="rank_box bg-white" style="margin: 0" v-for="(product,index) in brand.ranking" :key="index" :to="`/product/${product.업체별_제품코드}`">
        <div class="rank_order">{{ index + 1 }}</div>
        <div class="rank_image">
            <img class="rank_image" :src='`/media/product_images/${product.업체별_제품코드}.png`' alt="상품이미지" style="height: min(25vh, 25vw); width: min(25vh, 25vw);" />
        </div>
        <div class="rank_manufacturer">{{ product.업소명 }}</div>
        <div class="rank_name">{{ product.nutraceuticals_name }}</div>
        <div class="rank_score">
            온라인 <span style="color: #FFCC21;">★</span>{{ product.review.average_rating }}({{ product.review.total_reviews }}) 
            <span style="color: gainsboro;"> | </span>
            바름 <span style="color: #FFCC21;">★</span>{{ product.bareum_review.average_rating }}({{ product.bareum_review.total_reviews }})
        </div>
        <div class="rank_price">최저가 : {{ product.review.lowest }}원</div>
    </div>
</div>
<div ref="loader" class="loader"></div>
</div>
</template>

<script>
import { ref, computed,onMounted, onUnmounted } from 'vue';
import axios from "axios";

export default {
    setup() {
        const page = ref(1);
        const per_page = 10;
        const postTotalPages = ref(1);
        const loader = ref(null);
        const brandRanking = ref([]);

        const fetchBrandRanking = async() => {
            if(page.value <= postTotalPages.value){
                try{
                const response = await axios.get(`/api/product/brand-ranking/?page=${page.value}`);
                console.log(response.data);
                brandRanking.value.push(...response.data.results);
                postTotalPages.value = Math.ceil(response.data.count/ per_page);
                page.value+=1;
                }catch(err){
                    console.error(err);
                }
            }
            
        }

        
        let observer;

        onMounted(async () => {
            await fetchBrandRanking();
            
            observer = new IntersectionObserver(async (entries, observer) => {
            if (entries[0].isIntersecting) {
                await fetchBrandRanking();
            }
            });
        
            if (loader.value) {
            observer.observe(loader.value);
            }
        });
    
        onUnmounted(() => {
            if (loader.value) {
            observer.unobserve(loader.value);
            }
        });

        return {
            fetchBrandRanking,
            brandRanking,
            loader,

        };
    }
}
</script>

<style>
</style>