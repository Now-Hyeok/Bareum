import { createApp } from 'vue';
import { createPinia } from 'pinia';
import './style.css';
import App from './App.vue';
import router from './router.js';
import 'bootstrap';
import 'bootstrap/dist/css/bootstrap.min.css';
import axios from 'axios';
import InfiniteScroll from 'vue-infinite-scroll';
import csrf from './csrf';
import Cookies from 'js-cookie';
import { useUserInfo } from './stores';
axios.defaults.withCredentials = true;

const pinia = createPinia();
const app = createApp(App);

app.use(pinia);
app.use(router);
app.use(csrf);
app.use(InfiniteScroll);

const userInfo = useUserInfo;
const fetchUserInfo = async () =>{
  try {
    const response = await axios.get('/api/account/check_session/');
    if (response.data.logged_in) {
      // userInfo.serLogin(loginResult.member_id,loginResult.login_id,loginResult.username,loginResult.profile_img_url);
      // userInfo.userAddInfo(data.birthday,data.gender,data.nickname,data.weight, data.height);

    }
  } catch (error) {
    console.error(error);
    return null;
  }
}
fetchUserInfo();
app.mount('#app');
