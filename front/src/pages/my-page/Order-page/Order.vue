<template >
    <div class="container">
        <nav class="navbar fixed-top bg-white">
        <div class="container-fluid">
          <router-link to="/cart" class="navbar-brand" style="margin-left: 2vh;">
            <svg xmlns="http://www.w3.org/2000/svg" width="25" height="25" fill="black" class="bi bi-arrow-left" viewBox="0 0 16 16">
              <path fill-rule="evenodd" d="M15 8a.5.5 0 0 0-.5-.5H2.707l3.147-3.146a.5.5 0 1 0-.708-.708l-4 4a.5.5 0 0 0 0 .708l4 4a.5.5 0 0 0 .708-.708L2.707 8.5H14.5A.5.5 0 0 0 15 8z"/>
            </svg>
        </router-link>
        <div style="margin-right: 2vh;">주문/결제</div>
        <div to="/mysetting" class="navbar-brand" style="opacity: 0;">
          <svg xmlns="http://www.w3.org/2000/svg" width="25" height="25" fill="currentColor" class="bi bi-gear-fill" viewBox="0 0 16 16">
            <path d="M9.405 1.05c-.413-1.4-2.397-1.4-2.81 0l-.1.34a1.464 1.464 0 0 1-2.105.872l-.31-.17c-1.283-.698-2.686.705-1.987 1.987l.169.311c.446.82.023 1.841-.872 2.105l-.34.1c-1.4.413-1.4 2.397 0 2.81l.34.1a1.464 1.464 0 0 1 .872 2.105l-.17.31c-.698 1.283.705 2.686 1.987 1.987l.311-.169a1.464 1.464 0 0 1 2.105.872l.1.34c.413 1.4 2.397 1.4 2.81 0l.1-.34a1.464 1.464 0 0 1 2.105-.872l.31.17c1.283.698 2.686-.705 1.987-1.987l-.169-.311a1.464 1.464 0 0 1 .872-2.105l.34-.1c1.4-.413 1.4-2.397 0-2.81l-.34-.1a1.464 1.464 0 0 1-.872-2.105l.17-.31c.698-1.283-.705-2.686-1.987-1.987l-.311.169a1.464 1.464 0 0 1-2.105-.872l-.1-.34zM8 10.93a2.929 2.929 0 1 1 0-5.86 2.929 2.929 0 0 1 0 5.858z"/>
          </svg>
        </div>
        </div>
      </nav>

      
      <div class="mycard-container">
      <div class="card" style="width: 100%; padding:0;  display:block; box-shadow: 2px 2px 2px 2px #eeeeee">
        <div class="card-body">
          <div class="flex-grow-1 ms-3">
            <div class="d-flex flex-row align-items-center mb-2">
              <h2 class="mb-0 me-3" style="font-weight: bold;">배송지 정보</h2>
            </div>
          </div>
          <div style="display: flex; align-items: flex-end; flex-wrap: nowrap; margin-top: 5%;">
            <div style="width: 10vh; color:gray;"><span>수령인</span></div>
            <input type="text" placeholder=" "
              style="width: 80%; color: black; background-color: white; border: none; border-bottom: 1px solid gray;" v-model="receiver" readonly>
          </div>

          <div style="display: flex; align-items: flex-end; flex-wrap: nowrap; margin-top: 6%;">
            <div style="width: 10vh; color:gray;"><span>전화번호</span></div>
            <input type="text" placeholder=" "
              style="width: 80%; color: black; background-color: white; border: none; border-bottom: 1px solid gray;" v-model="phoneNumber" readonly>
          </div>

          <div style="display: flex; align-items: flex-end; flex-wrap: nowrap; margin-top: 6%;">
            <div style="width: 10vh; color:gray;"><span>우편번호</span></div>
            <input type="text" v-model="postcode" placeholder=" "
              style="width: 60%; background-color: white; color: black; border: none; border-bottom: 1px solid gray;" readonly>
          </div>

          <div style="display: flex; align-items: flex-end; flex-wrap: nowrap; margin-top: 6%;">
            <div style="width: 10vh; color:gray;"><span>주소</span></div>
            <input type="text" :value="address" readonly
              style="width: 80%; background-color: white; color:black; border: none; border-bottom: 1px solid gray;">
          </div>

          <div style="display: flex; align-items: flex-end; flex-wrap: nowrap; margin-top: 6%; margin-bottom: 2%">
            <div style="width: 10vh; color:gray;"><span>상세주소</span></div>
            <input type="text" id="detailAddress" placeholder=" "
              style="width: 80%; background-color: white; color:black; border: none; border-bottom: 1px solid gray;"
              v-model="detailed_address" readonly>
          </div>
        </div>
      </div>
    </div>
    <div class="mycard-container">
      <div class="card" style="width: 100%; padding:0;  display:block; box-shadow: 2px 2px 2px 2px #eeeeee">
        <div class="card-body">
          <div class="flex-grow-1 ms-3">
            <div class="d-flex flex-row align-items-center mb-2">
              <h2 class="mb-0 me-3" style="font-weight: bold;">주문 상품 정보</h2>
            </div>
          </div>
          <div style="display: flex; align-items: flex-end; flex-wrap: nowrap; margin-top: 5%;">
            <div v-for="(product,index) in orderProductList" :key="index">
              <p>{{ product.product.업소명 }}</p>
              <p>{{ product.product.nutraceuticals_name }}</p> 
              <p>{{ product.quantity }} 개 </p>
              <p>{{ product.lowest * product.quantity }} 원</p>
            </div>
          </div>
        </div>
        </div>
      </div>
      <div class="mycard-container">
      <div class="card" style="width: 100%; padding:0;  display:block; box-shadow: 2px 2px 2px 2px #eeeeee">
        <div class="card-body">
          <div class="flex-grow-1 ms-3">
            <div class="d-flex flex-row align-items-center mb-2">
              <h2 class="mb-0 me-3" style="font-weight: bold;">결제금액</h2>
            </div>
          </div>
          
          <div style="display: flex; margin-left: 5%; margin-right: 5%; justify-content: space-between;">
          <p style="text-align: left; color: gray;">총 상품 금액</p>
          <p style="text-align: right;">{{ totalAmount }} 원</p>
        </div>
        <div style="display: flex; margin-left: 5%; margin-right: 5%; justify-content: space-between;">
          <p style="text-align: left; color: gray;">배송비</p>
          <p style="text-align: right;">무료</p>
        </div>

        <div style="display: flex; margin-left: 5%; margin-right: 5%; justify-content: space-between;">
          <p style="text-align: left; color: gray;">최종 결제 금액</p>
          <p style="text-align: right;">{{ totalAmount }} 원</p>
        </div>
            

          
        </div>
        </div>
      </div>

    </div>


    <div>
        <button @click="payment" style="background-color: #2dce89; border-radius: 5px; color:white;">결제하기</button>
    </div>

</template>
<script>
import axios from 'axios';
import {ref,toRefs, onMounted,reactive} from 'vue';
import { useOrderStore, useUserInfo } from '../../../stores';
import Cookies from 'js-cookie';
import { useRouter } from 'vue-router';

export default {

    setup(){
        const router = useRouter();
        const csrf_token = Cookies.get("csrftoken");
        const userInfo = useUserInfo();
        const state = reactive({
          postcode: '',
          address: '',
          extraAddress: '',
          detailed_address: '',
          phoneNumber:'',
          receiver:''
        });
        const orderProductList = ref([]);
        const totalAmount = ref(0);
        const fetchAddress = async () => {
          try {
            const response = await axios.get(`/api/account/address/${userInfo.memberId}/`);
            state.postcode = response.data.postcode;
            state.address = response.data.address;
            state.extraAddress = response.data.extra_address;
            state.detailed_address = response.data.detailed_address;
            state.phoneNumber = response.data.phone_number;
            state.receiver = response.data.receiver;
          } catch (error) {
            console.error(error);
          }
        };

        onMounted(() => {

            fetchAddress();
            const orderStore =  useOrderStore();
            orderProductList.value = orderStore.orderList;
            totalAmount.value = orderStore.totalAmount;
        })

        const payment = async () => {
          if (window.confirm("결제하시겠습니까?")){
            try{
              window.alert("결제가 완료되었습니다");
              router.push('/mypage');
            }catch(err){
              window.alert("결제실패");

              console.error(err);
            }
          }
        }

        return{
          payment, 
            fetchAddress,
            ...toRefs(state),
            orderProductList,
            totalAmount
        }
    }
}
</script>
<style >
    
</style>