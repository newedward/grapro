<template>
  <div id="topNav">
    <el-header height="80px" >
      <el-avatar :src='avatar' style="margin-left: 100px;margin-top: 2%"></el-avatar>

        <el-button type="text" style="margin-left: 200px"  @click.native="jumpTo($event)" id="个人信息">个人信息</el-button>
        <el-button type="text" style="margin-left: 200px"  @click.native="jumpTo($event)" id="流程管理">流程管理</el-button>
        <el-button type="text" style="margin-left: 200px"  @click.native="jumpTo($event)" id="校园动态">校园动态</el-button>
        <el-button type="text" icon="el-icon-bell" circle style="margin-left: 200px;"  @click="checkMessage"></el-button>
        <el-button type="primary" @click="toLogin" v-if="userId==0" style="margin-left: 200px">登录</el-button>
    </el-header>
  </div>
</template>

<script>

/*
 * 该文件负责显示页面的topNav
 * 不接受任何参数
 */

export default {
  name: 'topNav',

  components: {
  },
    mounted: function(){
        this.getCurUserID()
    },
    data(){
      return {
          input1:'',
          avatar:'',
          userId:0
    }
    },

  methods:{
      getCurUserID(){
        this.$http.get('/api/getCurUserID')
                  .then((response)=>{
                    var res1 = JSON.parse(response.bodyText)
                      if(res1['err_num']==0){
                          this.userId=res1['userID'];
                          this.getCurUser()
                      }
              })
      },
      getCurUser(){
          this.$http.post('/api/getUserByID/',{'userId':this.userId},{emulateJSON:true})
              .then(function(response){
                    var res1 = JSON.parse(response.bodyText);
                    if(res1['err_num']==0){
                        this.avatar = res1["user"][0]["fields"]["avatar"];
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
          if(name=="个人信息"){
              window.location.href="/index";
          }
          else if(name=="流程管理"){

                  window.location.href="/process";
          }
          else if(name=="校园动态"){
              if(this.userId==0){
                  this.$message({type:'error',message:"请先登录！",duration:600})
              }
              else{
                  window.location.href="/home";
              }
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
  .el-header{
    background-color: #0b0b0b;
    color: 	#FFFFFF;
    margin-top: -15px;
    margin-left: -15px;
    margin-right: -15px;
    width: 1536px;
    /*box-shadow: 0 2px 12px 0 rgba(0, 0, 0, 0.1);*/
    text-align: center;
  }
</style>
