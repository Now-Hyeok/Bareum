<template>
    <div class="writecontainer">
      <nav class="navbar fixed-top bg-white">
        <div class="container-fluid">
          <router-link to="/community" class="navbar-brand" style="margin-left: 2vh;">
            <svg xmlns="http://www.w3.org/2000/svg" width="25" height="25" fill="black" class="bi bi-arrow-left" viewBox="0 0 16 16">
              <path fill-rule="evenodd" d="M15 8a.5.5 0 0 0-.5-.5H2.707l3.147-3.146a.5.5 0 1 0-.708-.708l-4 4a.5.5 0 0 0 0 .708l4 4a.5.5 0 0 0 .708-.708L2.707 8.5H14.5A.5.5 0 0 0 15 8z"/>
            </svg>
        </router-link>
        <div style="margin-right: 2vh;">글 작성</div>
        <div to="/mysetting" class="navbar-brand" style="opacity: 0;">
          <svg xmlns="http://www.w3.org/2000/svg" width="25" height="25" fill="currentColor" class="bi bi-gear-fill" viewBox="0 0 16 16">
            <path d="M9.405 1.05c-.413-1.4-2.397-1.4-2.81 0l-.1.34a1.464 1.464 0 0 1-2.105.872l-.31-.17c-1.283-.698-2.686.705-1.987 1.987l.169.311c.446.82.023 1.841-.872 2.105l-.34.1c-1.4.413-1.4 2.397 0 2.81l.34.1a1.464 1.464 0 0 1 .872 2.105l-.17.31c-.698 1.283.705 2.686 1.987 1.987l.311-.169a1.464 1.464 0 0 1 2.105.872l.1.34c.413 1.4 2.397 1.4 2.81 0l.1-.34a1.464 1.464 0 0 1 2.105-.872l.31.17c1.283.698 2.686-.705 1.987-1.987l-.169-.311a1.464 1.464 0 0 1 .872-2.105l.34-.1c1.4-.413 1.4-2.397 0-2.81l-.34-.1a1.464 1.464 0 0 1-.872-2.105l.17-.31c.698-1.283-.705-2.686-1.987-1.987l-.311.169a1.464 1.464 0 0 1-2.105-.872l-.1-.34zM8 10.93a2.929 2.929 0 1 1 0-5.86 2.929 2.929 0 0 1 0 5.858z"/>
          </svg>
        </div>
        </div>
      </nav>
      
      
      <form @submit.prevent="submitPost">
        <div class="writetitle" >
          <input id="title" placeholder="제목" style="width:100%; border: none; border-bottom: 1px solid #eeeeee;" v-model="postTitle" require/>
        </div>
        <div class="writecontent">
          <textarea id="content" placeholder="내용을 입력하세요" style=" width:100%; height: 20vh; border: none; border-bottom: 1px solid #eeeeee;" v-model="postContent" required ></textarea>
        </div>
        <div style="margin-top: 10%; text-align: left;">
          
          <div><input id="images" ref="imageInput" type="file" accept="image/*" multiple @change="previewImages" /></div>
        </div>
        <div style="margin-top: 5%; text-align: left;" v-for="(url, index) in imagePreviewUrls" :key="index">
          <img :src="url" class="preview-image" style="width:100%; height:30%;" />
          <button @click="removeImage(index)">x</button>
        </div>
        <button class="postbutton" type="submit" style="margin-top: 5%; border-radius: 10px; width:30%;">완료</button>
      </form>
    </div>
  </template>
  
  <script>
  import { ref, computed } from 'vue';
  import axios from 'axios';
  import { useUserInfo } from '../../stores';
  import { useRouter } from 'vue-router';
  import Cookies from 'js-cookie';

  export default {
    setup() {
      const postTitle = ref('');
      const postContent = ref('');
      const userInfo = useUserInfo();
      const router = useRouter();
      const csrf_token = Cookies.get('csrftoken');

      const imageInput = ref(null); // 이미지 input 참조를 위한 ref
      const selectedImageFiles = ref([]); // 선택된 이미지 파일 리스트 ref
      const imagePreviewUrls = ref([]); // 미리보기 이미지 URL ref
      const resizeImage = (file) => {
        const maxWidth = 800;
        const maxHeight = 800;
        const img = new Image();
        const canvas = document.createElement('canvas');
            
        return new Promise((resolve, reject) => {
          img.onload = () => {
            let width = img.width;
            let height = img.height;
          
            if (width > height) {
              if (width > maxWidth) {
                height *= maxWidth / width;
                width = maxWidth;
              }
            } else {
              if (height > maxHeight) {
                width *= maxHeight / height;
                height = maxHeight;
              }
            }
          
            canvas.width = width;
            canvas.height = height;
            canvas.getContext('2d').drawImage(img, 0, 0, width, height);
          
            canvas.toBlob(blob => {
              resolve(new File([blob], file.name, { type: file.type }));
            }, file.type);
          };
          img.onerror = (err) => reject(err);
          img.src = URL.createObjectURL(file);
        });
      };
      
      const previewImages = async () => {
        const files = Array.from(imageInput.value.files);
        const resizedFiles = [];
      
        for (const file of files) {
          try {
            const resizedFile = await resizeImage(file);
            resizedFiles.push(resizedFile);
          } catch (err) {
            console.error('Image resize failed:', err);
          }
        }
        
        selectedImageFiles.value = resizedFiles;
        imagePreviewUrls.value = resizedFiles.map(file => URL.createObjectURL(file));
      };
    const submitPost = async () => {
      try {
        const formData = new FormData();
        formData.append("title", postTitle.value);
        formData.append("content", postContent.value);
        formData.append("memberId", userInfo.memberId);
        // 이미지 파일 첨부 시 formData에 추가 (복수 파일 처리)
        selectedImageFiles.value.forEach((file, index) => {
          formData.append(`image${index}`, file);
        });
      
        await axios.post("/api/community/write", formData, {
          headers: {
            "Content-Type": "multipart/form-data", // 폼 데이터 전송을 위해 수정
            "X-CSRFToken": csrf_token,
          },
        });
      
        router.push("/community"); // 커뮤니티 페이지로 이동
      } catch (error) {
        console.error("글 작성 중 에러가 발생했습니다:", error);
      }
    };

      const removeImage = (index) => {
      // 미리보기 이미지 URL 리스트에서 해당 이미지 제거
      imagePreviewUrls.value.splice(index, 1);

      // 선택된 이미지 파일 리스트에서 해당 파일 제거
      selectedImageFiles.value.splice(index, 1);
    };

  
      return {
        postTitle,
        postContent,
        submitPost,
        
        imageInput,
        selectedImageFiles,
        imagePreviewUrls,
        previewImages,
        removeImage
        
      };
    },
  };
  </script>
  
  <style>
  .preview-image {
  width: 100px;
  height: 100px;
  object-fit: cover;
}
.writecontainer {
    width: 100%; /* 화면 너비에 꽉 차도록 설정 */
    height: 100%; /* 화면 높이에 꽉 차도록 설정 */
    display: block;
    border-radius: 10px;
    padding-top: 10%;
    padding-bottom: 20%;
  }

  .writetitle{
    width:100%;
    height:100%;
    display: block;
    margin-bottom: 5%;
  }
  </style>
  