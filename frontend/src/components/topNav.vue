<template>
<el-header height="60px">
    <div id="topNav" >

      <el-row type="flex"  justify="center" align="middle" >
        <el-col span="20" class="row-tn" >
          <el-avatar v-if="watchId" :src=avatar  style="margin-left:10%" ></el-avatar>

        <el-button type="text"  style="margin-left: 10%"  @click.native="jumpTo($event)" id="主页">主页</el-button>
        <el-button type="text" style="margin-left: 10%"  @click.native="jumpTo($event)" id="流程管理">流程管理</el-button>
        <el-button type="text"  style="margin-left: 10%" @click.native="jumpTo($event)" id="学校动态">学校动态</el-button>
          <el-button type="text" style="margin-left: 10%"  @click.native="jumpTo($event)" id="个人信息">个人信息</el-button>
        <el-button type="text" icon="el-icon-bell" style="margin-left: 10%"  @click="checkMessage"></el-button>
<el-button type="primary" @click="toLogin" v-if="!watchId" style="margin-left: 10%">登录</el-button>
          <el-button type="primary" @click="toLogin" v-if="watchId" style="margin-left: 10%">登出</el-button>
        </el-col>

        </el-row>
    </div></el-header>
</template>

<script>

/*
 * 该文件负责显示页面的topNav
 * 不接受任何参数
 */

export default {

  name: 'topNav',
  props:{
    watchId:{
      type: String,
      default: ''
    }
  },
  components: {
  },
    mounted: function(){
        this.getUserAvater()
    },
    data(){
      return {
          input1:'',
          avatar:'',
    }
    },

  methods:{
      getUserAvater(){
          this.$http.post('/api/getUserAvaterByID/',{'watchId':this.watchId},{emulateJSON:true})
              .then(function(response){
                    var res1 = JSON.parse(response.bodyText);
                    if(res1['err_num']==0){
                        this.avatar = res1["avater"];
                        console.log(this.avatar);
                    }

              })
      },
      onSearch: function(){
          if(this.input1==''){
              this.$message({type:'error',message:"请输入搜索内容！",duration:600})
          }
          else{
              window.location.href="/search/"+this.input1;
          }
      },
      jumpTo: function(e){
          var name=e.currentTarget.id;
          if(name=="主页"){
              window.location.href="/home";
          }
          else if(name=="流程管理"){
              // if(this.userId==0){
              //     this.$message({type:'error',message:"请先登录！",duration:600})
              // }
              // else{
                  window.location.href="process";
              // }
          }
          else if(name=="学校动态"){
              // if(this.userId==0){
              //     this.$message({type:'error',message:"请先登录！",duration:600})
              // }
              // else{
                  window.location.href="/home";
              // }
          }
          else if(name=="个人信息"){
              // if(this.userId==0){
              //     this.$message({type:'error',message:"请先登录！",duration:600})
              // }
              // else{
                  window.location.href="/personinfo";
              // }
          }
      },
      checkMessage: function() {
          if(this.userId==0){
                  this.$message({type:'error',message:"请先登录！",duration:600})
              }
          else{
              window.location.href="/message";
          }
      },
      userSettings(command) {
          if(command=='logout'){
            if( confirm("确定要退出？")) {
              this.$axios.post('/api/logout/')

              window.location.href = "/login";
            }
          }
          else window.location.href = "/edituser";      },
      toLogin: function () {
          window.location.href = "/login";      }

  }
}
</script>

<style>
  .el-header {
  background-color: rgb(254, 253, 252);
    width: 100%;
  }
  .el-avatar{

    vertical-align:middle;
  }
  #topNav{
    margin: 8px;
  }
  .row-tn {
    border-radius: 15px;
    box-shadow: 0 2px 12px 0 rgba(0, 0, 0, 0.1);
    /*text-align: center;*/
    /*margin: auto auto;*/
  }
</style>
