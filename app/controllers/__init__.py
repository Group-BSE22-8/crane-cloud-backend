# import all controllers

from .index import IndexView
from .users import (
    UsersView, UserLoginView, UserEmailVerificationView,
    EmailVerificationRequest, ForgotPasswordView, ResetPasswordView,
    UserDetailView, AdminLoginView, OAuthView, UserDataSummaryView, UserAdminUpdateView, UserStatusView, UserCountView, UserLogView)
from .deployments import DeploymentsView
from .clusters import (
    ClustersView, ClusterDetailView, ClusterNamespacesView,
    ClusterNamespaceDetailView, ClusterNodesView, ClusterNodeDetailView,
    ClusterDeploymentsView, ClusterDeploymentDetailView, ClusterPvcsView,
    ClusterPvcDetailView, ClusterPVsView, ClusterPVDetailView,
    ClusterPodsView, ClusterPodDetailView, ClusterServicesView,
    ClusterServiceDetailView, ClusterJobsView, ClusterJobDetailView,
    ClusterStorageClassView, ClusterStorageClassDetailView, ClusterCountView)
from .roles import RolesView, RolesDetailView
from .user_role import UserRolesView
from .project import (
    ProjectsView, ProjectDetailView, UserProjectsView,
    ProjectCPUView, ProjectMemoryUsageView, ProjectNetworkRequestView, ProjectStorageUsageView, ProjectStatusView, ProjectCountView, ProjectLogView, ProjectDBView, ProjectDBSView, SpecificProjectsView)
from .app import (AppsView, ProjectAppsView, AppDetailView, AppLogsView,
                  AppCpuUsageView, AppMemoryUsageView, AppNetworkUsageView, AppStorageUsageView,
                  AppDataSummaryView, AppRevertView, AppStatusView, AppCountView, AppLogView)
from .registry import RegistriesView
from .project_database import (ProjectDatabaseView, ProjectDatabaseDetailView, ProjectDatabaseAdminView,
                               ProjectDatabaseAdminDetailView, ProjectDatabaseResetView, ProjectDatabaseAdminResetView,
                               ProjectDatabasePasswordResetView, ProjectDatabaseAdminPasswordResetView,
                               ProjectDatabaseRetrievePasswordView, ProjectDatabaseAdminRetrievePasswordView, DatabaseStatsView)
from .log import LogsView
