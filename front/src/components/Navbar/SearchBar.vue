<template>
    <div class="search">
        <input class="search-input" type="text" :placeholder="placeholder" v-model="searchQuery" @keydown.enter="search">
        <svg v-show="searchQuery" class="clear-icon" style="width: 17px; right: 37px;" @click="searchbar_clear" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24">
            <path d="M19 6.41L17.59 5 12 10.59 6.41 5 5 6.41 10.59 12 5 17.59 6.41 19 12 13.41 17.59 19 19 17.59 13.41 12z"></path>
        </svg>
        <img class="search-icon" src="https://s3.ap-northeast-2.amazonaws.com/cdn.wecode.co.kr/icon/search.png" @click="search()">
    </div>
</template>

<script>
import { ref } from 'vue';

export default {
    emits: ['searchQuery'],
    props: {
        placeholder: {
            type: String,
            default: '검색어 입력',
        },
    },
    setup(props, context) {
        const searchQuery = ref(null);
    
        const search = () => {
            // 검색 로직
            context.emit('searchQuery', searchQuery.value);
            console.log('검색어:', searchQuery.value);
        };
        
        const searchbar_clear = () => {
            searchQuery.value = '';
        }
        const getQuery = (param) => {
            searchQuery.value = param;
        }

        if(props.query != '') {
            getQuery(props.query)
        }

        return {
            searchQuery,
            search,
            searchbar_clear,
            getQuery,
        };
    }
};
</script>

<style>
.search {
    position: relative;
    width: 100%;
    height: 100%;
    display: flex;
    align-items: center;
}

.search-input {
    width: 100%;
    border: 1px solid rgba(235, 242, 233, 1);
    border-radius: 8px;
    padding: 10px 12px;
    font-size: 14px;
    box-sizing : border-box;
    background-color: white;
    color: #333;
}

.search-icon {
    position: absolute;
    width: 17px;
    right: 12px;
    margin: 0;
   	z-index: 1;
}

.clear-icon {
    position: absolute;
    margin: 0;
   	z-index: 1;
}

</style>