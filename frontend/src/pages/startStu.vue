<template>
    <div id = "startStu">
       <el-container height= "100%" direction="vertical">
      <topNav></topNav>
      <el-container >
        <el-aside width="200px" style="background-color: rgb(238, 241, 246)">
        <flowStu></flowStu>
      </el-aside>
        <el-main>
          <el-row type="flex"  justify="center">
            <el-alert
    :title="status"
    :type="statusicon"
    :closable="false"
            center
            show-icon>
  </el-alert>

          </el-row>
          <el-row style="margin-bottom:20px">
            <el-col :span="8">
            <el-input v-model="title" placeholder="请输入内容"></el-input>
            </el-col>
            <el-col :span="6">
              <el-button round @click="addtitle" v-if="isnew">提交题目</el-button>
              <el-button v-else @click="changetitle">更换题目</el-button>
            </el-col>

      <el-button v-if="!isnew" type="success" @click="dialogVisible = true" :disabled="haspassed">点击提交开题相关文件</el-button>
    <el-tooltip v-show="haspassed" effect="dark" content="您的开题报告已经存档，无法重复提交" placement="top-start">
      <el-button style="float: right" type="info" icon="el-icon-question" circle></el-button>
    </el-tooltip>



          </el-row>
          <el-dialog
  title="提交"
  :visible="dialogVisible"
  width="30%"
  :before-close="handleClose">
            <el-row>
            <el-input type="textarea"
  :rows="8" v-model="introduction" placeholder="请输入提交说明（可以为空）"></el-input>
              </el-row>
            <el-row >
              <el-divider content-position="left">支持.doc/.docx/.pdf文件</el-divider>
              <el-upload
                :data="dataf"
                :headers="headerf"
                name = "work"
     accept=".doc, .docx, .pdf"
      action='/api/uploadfile/'
      :show-file-list="false"
      :on-success="handlefileSuccess"
      :before-upload="beforefileUpload"
      >
      <el-button size="small" type="primary">点击上传文件</el-button>

</el-upload>
            </el-row>
  <template #footer>
    <span class="dialog-footer">
      <el-button @click="dialogVisible = false">取 消</el-button>
      <el-button :disabled="uploaded" type="primary" @click="submit">确 定</el-button>
    </span>
  </template>
</el-dialog>

<el-collapse >
  <el-collapse-item v-for="(item,index) in list" :title="'第'+ (index+1) +'次提交'">
    <span class="check">{{item.content}}</span>
    <br>
    <!--<el-button size="mini">下载原始文件</el-button>-->
    <!--<el-button size="mini">下载评阅文件</el-button>-->
  </el-collapse-item>

</el-collapse>

        </el-main>
      </el-container>
    </el-container>
    </div>
</template>

<script>
  import topNav from '../components/topNav'
import flowStu from '../components/flowStu'

    export default {
        name: "startStu",
      components: {
      topNav,
      flowStu,
    },
      data(){
          return {
      dataf:{},
            headerf:{},
            title:"",
            workid:"",
            recordid:"",
            watchId:"",
            role:"",
            dialogVisible:false,
            uploaded:true,
            haspassed:false,
            status:"",
            statusicon:"",
            introduction:"",
            list:[
              // {content:"现实生活一致：与现实生活的流程、逻辑保持一致，遵循用户习惯的语言和概念；"},
              // {content:"简化流程：设计简洁直观的操作流程清晰明确：语言表达清晰且表意明确，让用户快速理解进而作出决策帮助用户识别：界面简单直白，让用户快速识别而非回忆，减少用户记忆负担"},
              // {content:"太好了"}
            ],
            isnew:""
  }
      },
      created(){

        this.getCurUserID()
      },
    methods: {
          addtitle(){
            this.$http.post('/api/addWorkTitle/',{'stuId':this.watchId,'title':this.title},{emulateJSON:true})
              .then(function(response){
                    var res1 = JSON.parse(response.bodyText);
                    if(res1['err_code']==0) {
                      this.workid = response['workid'];
                      this.isnew = false;
                      this.$message({
                      type: 'info',
                      message: '添加成功'
                        });
                      location.reload();
                    }
                    else{
                      this.$message.error("添加失败")
                    }

              })
          },
      changetitle(){
            console.log("TO DO");
      },
 beforefileUpload(file) {

    },
  handlefileSuccess(response, file, fileList) {
   // console.log(response);
   // console.log(file.raw);写一条记录
    this.$http.post('/api/addRecordStu/',{'stuId':this.watchId,'workId':this.workid,'path':response['path'],'process':'S'},{emulateJSON:true})
              .then(function(response){
                    var res1 = JSON.parse(response.bodyText);
                    if(res1['err_code']==0) {
                      this.dataf['next'] = this.dataf['next'] + 1;
                      this.recordid = res1["recordid"];
                      this.$message({
                      type: 'info',
                      message: '上传成功'
                        });
                      this.uploaded = false;
                    }
                    else{
                      this.$message.error("添加失败,请重试")
                    }

              })

    },
      getCurUserID(){
        this.$http.get('/api/getCurUserID')
                .then((response) => {
                  var res1 = JSON.parse(response.bodyText)
                  if (res1['err_num'] == 0) {
                    this.watchId = res1['userID'];
                    this.role = res1['role'];
                    this.getdata();
                  }
                })
      },
      getstatus(){
            this.$http.post('/api/getStudentStartProcess/',{'stuId':this.watchId},{emulateJSON:true})
              .then(function(response){
                 var res1 = JSON.parse(response.bodyText);
                this.status = res1["info"];
                 this.statusicon = res1["type"];
                 if (res1["statuscode"] >= 40){
                   this.haspassed = true;
                 }
              })
      },
      getdata(){
        //     读取record(list)和title
        // 设置布尔变量，进行修改或新增
            this.$http.post('/api/getRecordTitle/',{'stuId':this.watchId,'process':'S'},{emulateJSON:true})
              .then(function(response){
                    var res1 = JSON.parse(response.bodyText);
                    if(res1['err_code'] ==0) {
                      if(res1['title'] == "null"){
                        this.isnew = true;
                      }else{
                        this.isnew = false;
                        this.title = res1['title'];
                        this.workid = res1['workid'];
                      }
                      for (var i = 0;i<res1['rlist'].length;i++){
                        this.list.push({content:res1['rlist'][i]['fields']['content']})
                      }
                      this.dataf['next'] = this.list.length + 1;
                      this.dataf['stuid'] = this.watchId;
                      this.dataf['process'] = 'S';
                      this.getstatus();
                    }
                    else{
                      this.$message.error("获取信息失败")
                    }

              })
      },
      handleClose(done) {
        this.$confirm('确认关闭？')
          .then(_ => {
            this.dialogVisible= false;
            location.reload()
            done()
          })
          .catch(_ => {});
      },
      submit(){
            this.$http.post('/api/addRecordIntroduction/',{'recordId':this.recordid,'introduction':this.introduction},{emulateJSON:true})
              .then(function(response){
                    var res1 = JSON.parse(response.bodyText);
                    if(res1['err_code']==0) {
                      this.$message({
                      type: 'info',
                      message: '提交成功'
                        });
                      location.reload()
                    }
                    else{
                      this.$message.error("提交失败,请重试")
                    }

              })

      }

    }
    }
</script>

<style scoped>
.check{
  font-size: medium;
}
  /*#alert{*/
     /*box-shadow: 0 2px 4px rgba(0, 0, 0, .12), 0 0 6px rgba(0, 0, 0, .04);*/
    /**/
  /*}*/
</style>
