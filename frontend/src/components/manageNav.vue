<template>
<el-header height="60px">
    <div id="topNav" >

      <el-row type="flex"  justify="center" align="middle" >
        <el-col span="20" class="row-tn" >
          <el-avatar v-if="watchId" :src=avatar  style="margin-left:10%" ></el-avatar>

        <el-button type="text"  style="margin-left: 10%"  @click.native="jumpTo($event)" id="主页">主页</el-button>
        <el-button type="text" style="margin-left: 10%"  @click.native="jumpTo($event)" id="事件审批">事件审批</el-button>
        <el-button type="text"  style="margin-left: 10%" @click.native="jumpTo($event)" id="档案管理">档案管理</el-button>
          <el-button type="text" style="margin-left: 10%"  @click.native="jumpTo($event)" id="优秀毕设">优秀毕设</el-button>
        <el-button type="text" icon="el-icon-bell" style="margin-left: 10%"  @click="checkMessage"></el-button>
<el-button type="primary" @click="toLogin" v-if="!watchId" style="margin-left: 10%">登录</el-button>
          <el-button type="primary" @click="toLogout" v-if="watchId" style="margin-left: 10%">登出</el-button>
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

  name: 'manageNav',
  props:{
    watchId:{
      type: String,
      default: ''
    }
  },
  components: {
  },
    mounted: function(){
        this.getCurUserID();

    },
    data(){
      return {
          input1:'',
          avatar:'',
          role:'',
    }
    },

  methods:{
    getCurUserID(){
        this.$http.get('/api/getCurUserID')
                .then((response) => {
                  var res1 = JSON.parse(response.bodyText)
                  if (res1['err_num'] == 0) {
                    this.watchId = res1['userID'];
                    this.role = res1['role'];
                  }
                })
      },
      jumpTo: function(e){
          var name=e.currentTarget.id;
          if(name=="主页"){
              window.location.href="/home";
          }
          else if(name=="事件审批"){
                    window.location.href="checkMan";

          }
          else if(name=="档案管理"){
                  window.location.href="/fileMan";
          }
          else if(name=="优秀毕设"){
                  window.location.href="/greatMan";
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
      toLogin: function () {
          window.location.href = "/login";      },
      toLogout: function () {
         this.$http.get('/api/logout')
                .then((response) => {
                  var res1 = JSON.parse(response.bodyText)
                  if (res1['err_code'] == 0) {
                    location.reload()
                  }
                })
      }

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
