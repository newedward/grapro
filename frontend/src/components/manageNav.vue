<template>
<el-header height="60px">
    <div id="topNav">

      <el-row type="flex"  justify="center" align="middle" >
        <el-col span="20" class="row-tn" >
          <el-avatar v-if="watchId" :src=avatar  style="margin-left:10%" ></el-avatar>

        <el-button type="text"  style="margin-left: 10%"  @click.native="jumpTo($event)" id="主页">主页</el-button>
        <el-button type="text" style="margin-left: 10%"  @click.native="jumpTo($event)" id="事件审批">事件审批</el-button>
        <el-button type="text"  style="margin-left: 10%" @click.native="jumpTo($event)" id="档案管理">档案管理</el-button>
          <el-button type="text" style="margin-left: 10%"  @click="loginbacth" >批量注册</el-button>
        <el-button type="text"   @click="endnowopen" v-if="hasstart == 2">结束当前周期</el-button>
            <el-button type="text"   @click="startprocess" v-if="hasstart == 1" v-loading.fullscreen.lock="loading" element-loading-text="正在完成师生双选">结束师生互选</el-button>
            <el-button type="text"   @click="dialogVisible2 = true" v-if="hasstart == 0">开始当前周期</el-button>
<el-button type="primary" @click="toLogin" v-if="!watchId" style="margin-left: 10%">登录</el-button>
          <el-button type="primary" @click="toLogout" v-if="watchId" style="margin-left: 10%">登出</el-button>
        </el-col>

        </el-row>
      <el-dialog
  title="请上传文件批量注册"
  :visible="dialogVisible"l
  width="30%"
  :before-close="handleClose">

              <span>上传表格文件格式要求和相关说明：<br>
                1.如果标题为“学生”则代表批量注册学生账号，“导师”则代表批量注册导师账号<br>
                2.如果是学生必须有第一列（A列）是“学号”，第二列（B列）是“姓名”，如果是导师则需要第一列（A列）是“姓名”，第二列（B列）是“用户名”<br>
                3.为避免和其他学校的用户名重复，请输入后缀。注册好之后，学生账号的用户名和密码为学号加后缀，教师账号的密码和用户名为传入的用户名加后缀<br>
              4.如果出现其他情况导致注册失败，请联系开发人员</span>
<el-row>
            <el-input  v-model="suffix" placeholder="请输入后缀"></el-input>
              </el-row>
            <el-row >
              <el-divider content-position="left">支持.xls和xlsx文件</el-divider>
              <el-upload
                :data="dataf"
                :headers="headerf"
                name = "loginsheet"
     accept=".xls, .xlsx"
      action='/api/loginBacth/'
      :show-file-list="false"
      :on-success="handlefileSuccess"
      :before-upload="beforefileUpload"
      >
      <el-button size="small" type="primary">点击上传文件</el-button>

</el-upload>
            </el-row>
  <!--<template #footer>-->
    <!--<span class="dialog-footer">-->
      <!--<el-button @click="dialogVisible = false">取 消</el-button>-->
      <!--<el-button :disabled="uploaded" type="primary" @click="submit">确 定</el-button>-->
    <!--</span>-->
  <!--</template>-->
</el-dialog>
        <el-dialog
  title="开始本次毕设周期"
  :visible="dialogVisible2"
  width="30%"
  :before-close="handleClose2">

              <span>请输入每位导师最多能带的学生</span>
<el-row>
            <el-input  v-model="count"></el-input>
              </el-row>

            <el-button type="primary" @click="startnow">确 定</el-button>
</el-dialog>
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
        dialogVisible:false,
          dialogVisible2:false,
        dataf:{},
         headerf:{},
        suffix:'',
        watchId:'',
          hasstart:0,
          count:'',
          loading:false,
    }
    },

  methods:{
    getCurUserID(){
        this.$http.get('/api/getCurUserIDMan')
                .then((response) => {
                  var res1 = JSON.parse(response.bodyText)
                  if (res1['err_num'] == 0) {
                    this.watchId = res1['userID'];
                    this.role = res1['role'];
                    if (res1['avater'] == 0){
                        this.hasstart = 0;
                        this.count = res1['count'];
                    }
                    else if (res1['avater'] > 0){
                        this.hasstart = 1;
                        this.count = res1['count'];
                    }
                    else{
                        this.hasstart = 2
                    }
                  }
                })
      },
    loginbacth(){
      this.dialogVisible = true;
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
      },
    handleClose(done) {
        this.$confirm('确认关闭？')
          .then(_ => {
            this.dialogVisible= false;
            location.reload();
            done()
          })
          .catch(_ => {});
      },
      handleClose2(done) {
        this.$confirm('确认关闭？')
          .then(_ => {
            this.dialogVisible2= false;
            done()
          })
          .catch(_ => {});
      },
    handlefileSuccess(response, file, fileList){
      console.log(response['err_code'])
      if (response['err_code'] == 0) {
        this.dialogVisible = false;
                    this.$message({
                      type: 'success',
                      message: '批量注册成功'
                        });
                  }
      else if (response['err_code'] == 1){
        this.$message({
                      type: 'error',
                      message: '出现用户名重复问题，请更改后缀'
                        });
      }
      else if(response['err_code'] == -1){
        this.$message({
                      type: 'error',
                      message: '文件名错误'
                        });
      }


    },
    beforefileUpload(){
      this.dataf['manid'] = this.watchId;
      this.dataf['suffix'] = this.suffix;
    },
      startnow(){
        this.$http.post('/api/startnow/',{'manId':this.watchId,'count':this.count},{emulateJSON:true})
              .then(function(response){
                 var res1 = JSON.parse(response.bodyText);
                 if(res1["err_code"] == 0){
                     this.$message({
                      type: 'success',
                      message: '成功开始'
                        });
                     this.hasstart = 1;
                     location.reload();
                 }

              })
      },
      startprocess(){
    this.loading = true;
        this.$http.post('/api/startprocess/',{'manId':this.watchId},{emulateJSON:true})
              .then(function(response){
                 var res1 = JSON.parse(response.bodyText);
                 if(res1["err_code"] == 0){
                     this.$message({
                      type: 'success',
                      message: '操作成功'
                        });
                     this.hasstart = 2;
                     this.loading = false;
                 }

              })
      },
      endnowopen(){
        this.$confirm('此操作将结束本毕设周期, 是否继续?', '提示', {
          confirmButtonText: '确定',
          cancelButtonText: '取消',
          type: 'warning'
        }).then(() => {
          this.$http.post('/api/endnow/',{'manId':this.watchId},{emulateJSON:true})
              .then(function(response){
                 var res1 = JSON.parse(response.bodyText);
                 if(res1["err_code"] == 0){
                     this.$message({
                      type: 'success',
                      message: '操作成功'
                        });
                     this.hasstart = 0;
                     location.reload();
                 }

              })
        }).catch(() => {
          this.$message({
            type: 'info',
            message: '已取消结束'
          });
        });
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
