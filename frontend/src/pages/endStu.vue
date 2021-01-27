<template>
    <div id = "endStu">
       <el-container height= "100%" direction="vertical">
      <topNav></topNav>
      <el-container >
        <el-aside width="200px" style="background-color: rgb(238, 241, 246)">
        <flowStu></flowStu>
      </el-aside>
        <el-main>
          <el-row style="margin-bottom:20px">
            <el-col span="6"><el-button round>打印开题表格</el-button></el-col>
            <el-col span="6">
              <el-upload
     accept=".doc, .docx, .pdf"
      action="#"
      :before-upload="beforeAvatarUpload"
      :http-request="getfileUpload"
      :on-change="getValChange"
      :file-list="fileList"
      >
      <el-button size="small" type="primary">点击上传</el-button>
      <span style="margin-left:10px">支持.doc/.docx/.pdf文件</span>
</el-upload>
            </el-col>
          </el-row>
<el-collapse >
  <el-collapse-item v-for="(item,index) in list" :title="'第'+ (index+1) +'次提交'">
    <span class="check">{{item.content}}</span>
    <br>
    <el-button size="mini">下载原始文件</el-button>
    <el-button size="mini">下载评阅文件</el-button>
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
        name: "endStu",
      components: {
      topNav,
      flowStu,
    },
      data(){
          return {
      fileList: [],
            list:[
              {content:"现实生活一致：与现实生活的流程、逻辑保持一致，遵循用户习惯的语言和概念；"},
              {content:"简化流程：设计简洁直观的操作流程清晰明确：语言表达清晰且表意明确，让用户快速理解进而作出决策帮助用户识别：界面简单直白，让用户快速识别而非回忆，减少用户记忆负担"},
              {content:"太好了"}
            ]
  }
      },
    methods: {
          fileUpload(data){
    let url = '/card/scrapApply/uploadScrapCards';
    return postResponse(url,data,{contentType:'form'})
 },
      // 上传触发前 对文件格式的校验只校验了excel文件
 beforeAvatarUpload(file) {
      let FileExt = file.name.replace(/.+\./, "").toLowerCase();
      let flag = ["doc", "docx","pdf"].includes(FileExt);
      if (!flag) this.$message.error("只能上传doc\\docx\\pdf文件!");
      return flag;
    },
// 文件值改变时触发 change事件
    getValChange(file, fileList) {
      if (fileList.length > 0) {
        this.fileList = [fileList[fileList.length - 1]]
      }else{
        this.fileList = fileList[0]
      }
    },
  // 上传调用后台接口
  getfileUpload() {
      let formData = new FormData();
      formData.append("file",  this.fileList[0].raw);
      this.fileUpload(formData).then((res) => {
        this.$message.success("上传成功!");
      });
    },
    }
    }
</script>

<style scoped>
.check{
  font-size: medium;
}
</style>
